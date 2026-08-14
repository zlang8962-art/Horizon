import asyncio
import json
from datetime import datetime, timezone
from types import SimpleNamespace

import pytest
import src.ai.analyzer as analyzer_module
from tenacity import RetryError, retry, stop_after_attempt, wait_none
from src.ai.analyzer import ContentAnalyzer
from src.models import ContentItem, SourceType


def _make_item(item_id: str) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=f"Item {item_id}",
        url="https://example.com/item",
        published_at=datetime(2026, 4, 26, tzinfo=timezone.utc),
    )


def test_analyze_batch_does_not_sleep_by_default(monkeypatch):
    analyzer = ContentAnalyzer(SimpleNamespace())
    items = [_make_item("rss:test:1"), _make_item("rss:test:2")]
    sleep_calls = []

    async def fake_analyze_item(item):
        item.ai_score = 8.0

    async def fake_sleep(seconds):
        sleep_calls.append(seconds)

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)
    monkeypatch.setattr(analyzer_module.asyncio, "sleep", fake_sleep)

    result = asyncio.run(analyzer.analyze_batch(items))

    assert len(result) == 2
    assert sleep_calls == []


def test_analyze_batch_sleeps_between_items_when_throttle_configured(monkeypatch):
    client = SimpleNamespace(config=SimpleNamespace(throttle_sec=1.5))
    analyzer = ContentAnalyzer(client)
    items = [_make_item("rss:test:1"), _make_item("rss:test:2"), _make_item("rss:test:3")]
    sleep_calls = []

    async def fake_analyze_item(item):
        item.ai_score = 8.0

    async def fake_sleep(seconds):
        sleep_calls.append(seconds)

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)
    monkeypatch.setattr(analyzer_module.asyncio, "sleep", fake_sleep)

    asyncio.run(analyzer.analyze_batch(items))

    assert sleep_calls == [1.5, 1.5]


def test_analyze_batch_concurrent_processing(monkeypatch):
    """Verify that higher concurrency allows overlapping item processing."""
    client = SimpleNamespace(config=SimpleNamespace(analysis_concurrency=3))
    analyzer = ContentAnalyzer(client)
    items = [_make_item(f"rss:test:{i}") for i in range(5)]
    active_count = 0
    max_active = 0

    async def fake_analyze_item(item):
        nonlocal active_count, max_active
        active_count += 1
        max_active = max(max_active, active_count)
        await asyncio.sleep(0.05)  # Small delay to allow overlap
        active_count -= 1

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)

    asyncio.run(analyzer.analyze_batch(items))

    assert max_active == 3
    assert all(item.ai_score is None for item in items)  # None because fake_analyze_item doesn't set it


def test_analyze_batch_concurrent_preserves_order(monkeypatch):
    """Verify that analyze_batch preserves input order in results."""
    client = SimpleNamespace(config=SimpleNamespace(analysis_concurrency=3))
    analyzer = ContentAnalyzer(client)
    items = [_make_item(f"rss:test:{i}") for i in range(5)]

    async def fake_analyze_item(item):
        item.ai_score = float(item.id.split(":")[-1]) * 10

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)

    result = asyncio.run(analyzer.analyze_batch(items))

    assert [item.id for item in result] == [item.id for item in items]


def test_analyze_batch_provider_failure_stays_unscored(monkeypatch):
    analyzer = ContentAnalyzer(SimpleNamespace())
    item = _make_item("rss:test:provider-failure")

    async def fail_analysis(input_item):
        raise RuntimeError("provider unavailable")

    monkeypatch.setattr(analyzer, "_analyze_item", fail_analysis)

    result = asyncio.run(analyzer.analyze_batch([item]))

    assert result == [item]
    assert item.ai_score is None
    assert item.ai_scores == {}
    assert item.ai_reason is None
    assert item.ai_analysis_error == "AI analysis failed (RuntimeError; attempts=1)"
    assert item.ai_analysis_failure is not None
    assert item.ai_analysis_failure.model_dump() == {
        "error_type": "RuntimeError",
        "attempts": 1,
        "retryable": False,
        "http_status": None,
        "provider_error_code": None,
        "request_id": None,
    }


class _ProviderStatusError(RuntimeError):
    def __init__(
        self,
        status_code: int,
        *,
        body: object = None,
        request_id: object = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__("provider response body must never be persisted")
        self.status_code = status_code
        self.body = body
        self.request_id = request_id
        self.response = SimpleNamespace(headers=headers or {})


def test_analysis_failure_diagnostic_unwraps_retry_error_without_payloads():
    error = _ProviderStatusError(
        429,
        body={"code": 1302, "message": "sk-should-not-be-saved"},
        request_id="req_safe-123",
    )

    @retry(stop=stop_after_attempt(3), wait=wait_none())
    def fail_three_times() -> None:
        raise error

    with pytest.raises(RetryError) as raised:
        fail_three_times()

    diagnostic = analyzer_module._build_analysis_failure_diagnostic(raised.value)

    assert diagnostic.model_dump() == {
        "error_type": "_ProviderStatusError",
        "attempts": 3,
        "retryable": True,
        "http_status": 429,
        "provider_error_code": "1302",
        "request_id": "req_safe-123",
    }
    serialized = json.dumps(diagnostic.model_dump())
    assert "sk-should-not-be-saved" not in serialized
    assert "provider response body" not in serialized
    assert analyzer_module._safe_diagnostic_token("SK-secret-value") is None


def test_analysis_retry_policy_retries_only_transient_errors(monkeypatch):
    monkeypatch.setattr(analyzer_module.random, "uniform", lambda *_: 1.0)
    rate_limited = _ProviderStatusError(429)
    account_rate_limited = _ProviderStatusError(429, body={"code": 1302})
    platform_overloaded = _ProviderStatusError(429, body={"code": 1305})
    transient = _ProviderStatusError(503)
    invalid_request = _ProviderStatusError(400)

    assert analyzer_module._is_retryable_analysis_exception(rate_limited)
    assert analyzer_module._is_retryable_analysis_exception(transient)
    assert not analyzer_module._is_retryable_analysis_exception(invalid_request)

    rate_state = SimpleNamespace(
        outcome=SimpleNamespace(exception=lambda: rate_limited),
        attempt_number=1,
    )
    transient_state = SimpleNamespace(
        outcome=SimpleNamespace(exception=lambda: transient),
        attempt_number=1,
    )
    account_rate_limit_state = SimpleNamespace(
        outcome=SimpleNamespace(exception=lambda: account_rate_limited),
        attempt_number=1,
    )
    platform_overload_state = SimpleNamespace(
        outcome=SimpleNamespace(exception=lambda: platform_overloaded),
        attempt_number=1,
    )
    retry_after_state = SimpleNamespace(
        outcome=SimpleNamespace(
            exception=lambda: _ProviderStatusError(
                429,
                headers={"retry-after": "17"},
            )
        ),
        attempt_number=1,
    )

    assert analyzer_module._analysis_retry_wait(rate_state) == 10.0
    assert analyzer_module._analysis_retry_wait(transient_state) == 2.0
    assert analyzer_module._analysis_retry_wait(account_rate_limit_state) == 30.0
    assert analyzer_module._analysis_retry_wait(platform_overload_state) == 15.0
    assert analyzer_module._analysis_retry_wait(retry_after_state) == 17.0


class _RetryManagedFailureClient:
    def __init__(self, error: Exception) -> None:
        self.error = error
        self.calls = 0

    async def complete_for_retrying_caller(self, **kwargs):  # type: ignore[no-untyped-def]
        self.calls += 1
        raise self.error


def test_analyzer_applies_single_retry_policy_to_retry_managed_client():
    rate_limited = _ProviderStatusError(
        429,
        headers={"retry-after": "0.001"},
    )
    rate_limited_client = _RetryManagedFailureClient(rate_limited)
    rate_limited_item = _make_item("rss:test:rate-limited")

    asyncio.run(
        ContentAnalyzer(rate_limited_client).analyze_batch([rate_limited_item])
    )

    assert rate_limited_client.calls == 3
    assert rate_limited_item.ai_analysis_failure is not None
    assert rate_limited_item.ai_analysis_failure.attempts == 3
    assert rate_limited_item.ai_analysis_failure.http_status == 429

    invalid_request = _ProviderStatusError(400)
    invalid_request_client = _RetryManagedFailureClient(invalid_request)
    invalid_request_item = _make_item("rss:test:invalid-request")

    asyncio.run(
        ContentAnalyzer(invalid_request_client).analyze_batch([invalid_request_item])
    )

    assert invalid_request_client.calls == 1
    assert invalid_request_item.ai_analysis_failure is not None
    assert invalid_request_item.ai_analysis_failure.attempts == 1
    assert invalid_request_item.ai_analysis_failure.http_status == 400


def test_analyze_item_accepts_valid_result():
    result = {
        "score": 8.5,
        "reason": "Relevant",
        "summary": "A useful update",
        "tags": ["ai", "research"],
    }
    client = SimpleNamespace(complete=lambda **kwargs: None)

    async def complete(**kwargs):
        return json.dumps(result)

    client.complete = complete
    item = _make_item("rss:test:valid")

    asyncio.run(ContentAnalyzer(client)._analyze_item(item))

    assert item.ai_score == 8.5
    assert item.ai_reason == "Relevant"
    assert item.ai_summary == "A useful update"
    assert item.ai_tags == ["ai", "research"]


@pytest.mark.parametrize(
    "result",
    [
        {"score": 11, "reason": "high", "summary": "summary", "tags": []},
        {"score": float("nan"), "reason": "bad", "summary": "summary", "tags": []},
        {"score": 5, "reason": 123, "summary": "summary", "tags": []},
        {"score": 5, "reason": "ok", "summary": "summary", "tags": ["ok", 1]},
        {"score": 5, "reason": "ok", "tags": []},
    ],
)
def test_analyze_item_malformed_json_result_stays_unscored(result):
    async def complete(**kwargs):
        return json.dumps(result)

    item = _make_item("rss:test:invalid")

    asyncio.run(ContentAnalyzer(SimpleNamespace(complete=complete))._analyze_item(item))

    assert item.ai_score is None
    assert item.ai_scores == {}
    assert item.ai_reason is None
    assert item.ai_summary == item.title
    assert item.ai_tags == []
    assert item.ai_analysis_error
