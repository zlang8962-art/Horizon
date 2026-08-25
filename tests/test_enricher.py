"""Regression tests for enrichment retry, safety, and Chinese quality guards."""

import asyncio
import json
from datetime import datetime, timezone
from types import SimpleNamespace

from src.ai.enricher import ContentEnricher
from src.ai.prompts import CONCEPT_EXTRACTION_SYSTEM, CONTENT_ENRICHMENT_SYSTEM
from src.models import ContentItem, SourceType


def _item() -> ContentItem:
    return ContentItem(
        id="rss:test:enrichment",
        source_type=SourceType.RSS,
        title="Provider update",
        url="https://example.com/update",
        content="Source content that must not appear in diagnostics.",
        published_at=datetime(2026, 8, 25, tzinfo=timezone.utc),
        ai_score=9.0,
        ai_reason="Relevant",
        ai_summary="An English summary that may be retried only when safe.",
    )


class _ProviderStatusError(RuntimeError):
    def __init__(
        self,
        status_code: int,
        *,
        body: object = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__("provider payload must never be persisted")
        self.status_code = status_code
        self.body = body
        self.request_id = "req_enrichment-safe"
        self.response = SimpleNamespace(headers=headers or {})


class _ContentSafetyClient:
    def __init__(self) -> None:
        self.calls: list[str] = []
        self.config = SimpleNamespace(enrichment_concurrency=1)

    async def complete_for_retrying_caller(self, *, system: str, user: str) -> str:
        self.calls.append(system)
        if system == CONCEPT_EXTRACTION_SYSTEM:
            return json.dumps({"queries": []})
        raise _ProviderStatusError(
            400,
            body={"error": {"code": "1301", "message": "sk-do-not-persist"}},
        )


def test_enricher_marks_content_safety_without_resubmitting_to_translation() -> None:
    client = _ContentSafetyClient()
    item = _item()

    asyncio.run(ContentEnricher(client).enrich_batch([item]))

    assert client.calls == [CONCEPT_EXTRACTION_SYSTEM, CONTENT_ENRICHMENT_SYSTEM]
    assert item.ai_enrichment_failure is not None
    assert item.ai_enrichment_failure.model_dump() == {
        "error_type": "_ProviderStatusError",
        "attempts": 1,
        "retryable": False,
        "http_status": 400,
        "provider_error_code": "1301",
        "provider_error_category": "content_safety",
        "request_id": "req_enrichment-safe",
        "stage": "enrichment",
        "fallback": "content_safety_notice",
    }
    assert item.metadata["detailed_summary_zh"].startswith("该条资讯的中文内容暂不可用")
    assert item.metadata["zh_output_incomplete"] is True
    serialized = json.dumps(item.model_dump(mode="json"))
    assert "sk-do-not-persist" not in serialized
    assert "provider payload" not in serialized


class _RateLimitThenTranslateClient:
    def __init__(self) -> None:
        self.content_attempts = 0
        self.translation_attempts = 0
        self.config = SimpleNamespace(enrichment_concurrency=1)

    async def complete_for_retrying_caller(self, *, system: str, user: str) -> str:
        if system == CONCEPT_EXTRACTION_SYSTEM:
            return json.dumps({"queries": []})
        if system == CONTENT_ENRICHMENT_SYSTEM:
            self.content_attempts += 1
            raise _ProviderStatusError(
                429,
                body={"code": "1305", "message": "sk-do-not-persist"},
                headers={"retry-after": "0.001"},
            )
        self.translation_attempts += 1
        return json.dumps(
            {
                "title_zh": "模型服务暂时繁忙",
                "summary_zh": "该条资讯的中文摘要已通过受控降级生成。",
            }
        )


def test_enricher_uses_single_retry_policy_then_translates_after_rate_limit() -> None:
    client = _RateLimitThenTranslateClient()
    item = _item()

    asyncio.run(ContentEnricher(client).enrich_batch([item]))

    assert client.content_attempts == 3
    assert client.translation_attempts == 1
    assert item.ai_enrichment_failure is not None
    assert item.ai_enrichment_failure.attempts == 3
    assert item.ai_enrichment_failure.provider_error_code == "1305"
    assert item.ai_enrichment_failure.provider_error_category == "provider_overloaded"
    assert item.ai_enrichment_failure.fallback == "translated"
    assert item.metadata["detailed_summary_zh"] == "该条资讯的中文摘要已通过受控降级生成。"
    assert item.metadata["zh_output_incomplete"] is True


class _EnglishZhResponseClient:
    def __init__(self) -> None:
        self.translation_attempts = 0
        self.config = SimpleNamespace(enrichment_concurrency=1)

    async def complete_for_retrying_caller(self, *, system: str, user: str) -> str:
        if system == CONCEPT_EXTRACTION_SYSTEM:
            return json.dumps({"queries": []})
        if system == CONTENT_ENRICHMENT_SYSTEM:
            return json.dumps(
                {
                    "title_en": "English title",
                    "title_zh": "English title leaked",
                    "whats_new_en": "English summary",
                    "whats_new_zh": "English summary leaked",
                    "background_en": "English background",
                    "background_zh": "English background leaked",
                    "community_discussion_en": "English discussion",
                    "community_discussion_zh": "English discussion leaked",
                }
            )
        self.translation_attempts += 1
        return json.dumps(
            {
                "title_zh": "中文标题",
                "summary_zh": "中文摘要替代了错误的英文中文字段。",
            }
        )


def test_enricher_replaces_non_chinese_zh_summary_with_translation() -> None:
    client = _EnglishZhResponseClient()
    item = _item()

    asyncio.run(ContentEnricher(client).enrich_batch([item]))

    assert client.translation_attempts == 1
    assert item.ai_enrichment_failure is not None
    assert item.ai_enrichment_failure.error_type == "MissingChineseEnrichmentSummaryError"
    assert item.ai_enrichment_failure.fallback == "translated"
    assert item.metadata["title_zh"] == "中文标题"
    assert item.metadata["detailed_summary_zh"] == "中文摘要替代了错误的英文中文字段。"
    assert "background_zh" not in item.metadata
    assert "community_discussion_zh" not in item.metadata
