import asyncio
import json
from datetime import datetime, timezone
from types import SimpleNamespace

import pytest
from rich.console import Console

from src.models import AIConfig, Config, ContentItem, FilteringConfig, SourceType, SourcesConfig
from src.orchestrator import HorizonOrchestrator, TimeWindow
from src.storage.manager import StorageManager


def make_item(
    item_id: str,
    published_at: datetime,
    *,
    score: float | None = None,
) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=f"Title {item_id}",
        url=f"https://example.com/releases/{item_id}?token=do-not-store#details",
        content="PRIVATE ARTICLE BODY",
        published_at=published_at,
        metadata={"feed_name": "Example Feed", "category": "ai-tools"},
        ai_score=score,
    )


def test_candidate_audit_omits_bodies_and_url_queries(tmp_path) -> None:
    filtering = FilteringConfig(
        ai_score_threshold=7.0,
        candidate_audit_enabled=True,
    )
    storage = StorageManager(data_dir=str(tmp_path / "data"))
    orchestrator = HorizonOrchestrator.__new__(HorizonOrchestrator)
    orchestrator.config = SimpleNamespace(filtering=filtering)
    orchestrator.storage = storage
    orchestrator.console = Console(record=True)
    orchestrator.last_fetch_report = None
    published_at = datetime(2026, 7, 27, 8, 0, tzinfo=timezone.utc)
    item = make_item("selected", published_at, score=9.0)
    below_threshold = make_item("below-threshold", published_at, score=6.0)
    window = TimeWindow(
        since=datetime(2026, 7, 26, 16, 0, tzinfo=timezone.utc),
        until=datetime(2026, 7, 27, 16, 0, tzinfo=timezone.utc),
        report_date="2026-07-28",
        content_date="2026-07-27",
        mode="previous_calendar_day",
        timezone_name="Asia/Shanghai",
    )

    filtering_result = asyncio.run(
        orchestrator.filter_items(
            [item, below_threshold],
            topic_dedup=False,
            apply_balance=False,
            log=False,
        )
    )
    balanced_digest = orchestrator.apply_balanced_digest(
        filtering_result.items,
        log=False,
    )

    path = orchestrator._save_candidate_audit(
        window,
        state="completed",
        fetched_items=[item, below_threshold],
        in_window_items=[item, below_threshold],
        merged_items=[item, below_threshold],
        analyzed_items=[item, below_threshold],
        filtering_result=filtering_result,
        post_expansion_result=filtering_result,
        balanced_digest=balanced_digest,
    )

    assert path == storage.audits_dir / "2026-07-28-candidate-audit.json"
    serialized = path.read_text(encoding="utf-8")
    payload = json.loads(serialized)
    assert "PRIVATE ARTICLE BODY" not in serialized
    assert "do-not-store" not in serialized
    candidates = {candidate["id"]: candidate for candidate in payload["candidates"]}
    assert candidates["selected"]["url"] == "https://example.com/releases/selected"
    assert candidates["selected"]["decision"] == "selected"
    assert candidates["selected"]["reason"] == "selected"
    assert candidates["below-threshold"]["decision"] == "excluded"
    assert candidates["below-threshold"]["reason"] == "below_threshold"


def test_run_audits_items_outside_calendar_window(tmp_path, monkeypatch) -> None:
    filtering = FilteringConfig(
        time_window_mode="previous_calendar_day",
        time_window_timezone="Asia/Shanghai",
        candidate_audit_enabled=True,
    )
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
            languages=[],
        ),
        sources=SourcesConfig(),
        filtering=filtering,
    )
    storage = StorageManager(data_dir=str(tmp_path / "data"))
    orchestrator = HorizonOrchestrator(config, storage)
    window = TimeWindow(
        since=datetime(2026, 7, 26, 16, 0, tzinfo=timezone.utc),
        until=datetime(2026, 7, 27, 16, 0, tzinfo=timezone.utc),
        report_date="2026-07-28",
        content_date="2026-07-27",
        mode="previous_calendar_day",
        timezone_name="Asia/Shanghai",
    )
    outside = make_item(
        "outside",
        datetime(2026, 7, 28, 8, 0, tzinfo=timezone.utc),
    )

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        return [outside]

    monkeypatch.setattr(orchestrator, "_determine_time_window", lambda *args: window)
    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)

    asyncio.run(orchestrator.run())

    path = storage.audits_dir / "2026-07-28-candidate-audit.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["state"] == "no_content_in_window"
    assert payload["counts"]["fetched"] == 1
    assert payload["counts"]["in_window"] == 0
    assert payload["candidates"][0]["reason"] == "outside_window"


def test_run_audits_excessive_partial_analysis_failures(
    tmp_path,
    monkeypatch,
) -> None:
    filtering = FilteringConfig(
        max_analysis_failure_ratio=0.5,
        candidate_audit_enabled=True,
    )
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
            languages=[],
        ),
        sources=SourcesConfig(),
        filtering=filtering,
    )
    storage = StorageManager(data_dir=str(tmp_path / "data"))
    orchestrator = HorizonOrchestrator(config, storage)
    window = TimeWindow(
        since=datetime(2026, 7, 26, 16, 0, tzinfo=timezone.utc),
        until=datetime(2026, 7, 27, 16, 0, tzinfo=timezone.utc),
        report_date="2026-07-28",
        content_date="2026-07-27",
        mode="previous_calendar_day",
        timezone_name="Asia/Shanghai",
    )
    items = [
        make_item(
            f"item-{index}",
            datetime(2026, 7, 27, index, 0, tzinfo=timezone.utc),
        )
        for index in range(4)
    ]

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        return items

    async def analyze_content(input_items):  # type: ignore[no-untyped-def]
        for item in input_items[:3]:
            item.ai_analysis_error = "AI analysis failed after retries"
        input_items[3].ai_score = 9.0
        return input_items

    monkeypatch.setattr(orchestrator, "_determine_time_window", lambda *args: window)
    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)
    monkeypatch.setattr(orchestrator, "_analyze_content", analyze_content)

    with pytest.raises(RuntimeError, match="AI analysis failure ratio 3/4"):
        asyncio.run(orchestrator.run())

    path = storage.audits_dir / "2026-07-28-candidate-audit.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["state"] == "ai_analysis_failure_ratio_exceeded"
    assert payload["counts"]["analysis_failed"] == 3
    assert payload["analysis_quality"] == {
        "failure_ratio": 0.75,
        "max_failure_ratio": 0.5,
    }


def test_calendar_run_uses_report_date_and_shows_content_date(
    tmp_path,
    monkeypatch,
) -> None:
    filtering = FilteringConfig(
        ai_score_threshold=7.0,
        time_window_mode="previous_calendar_day",
        time_window_timezone="Asia/Shanghai",
        candidate_audit_enabled=True,
    )
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
            languages=["zh"],
        ),
        sources=SourcesConfig(),
        filtering=filtering,
    )
    storage = StorageManager(data_dir=str(tmp_path / "data"))
    orchestrator = HorizonOrchestrator(config, storage)
    window = TimeWindow(
        since=datetime(2026, 7, 26, 16, 0, tzinfo=timezone.utc),
        until=datetime(2026, 7, 27, 16, 0, tzinfo=timezone.utc),
        report_date="2026-07-28",
        content_date="2026-07-27",
        mode="previous_calendar_day",
        timezone_name="Asia/Shanghai",
    )
    item = make_item(
        "inside",
        datetime(2026, 7, 26, 17, 0, tzinfo=timezone.utc),
        score=9.0,
    )

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        return [item]

    async def analyze_content(items):  # type: ignore[no-untyped-def]
        return items

    async def enrich_items(items):  # type: ignore[no-untyped-def]
        return None

    monkeypatch.setattr(orchestrator, "_determine_time_window", lambda *args: window)
    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)
    monkeypatch.setattr(orchestrator, "_analyze_content", analyze_content)
    monkeypatch.setattr(orchestrator, "_enrich_important_items", enrich_items)
    monkeypatch.chdir(tmp_path)

    asyncio.run(orchestrator.run())

    summary_path = storage.summaries_dir / "horizon-2026-07-28-zh.md"
    summary = summary_path.read_text(encoding="utf-8")
    assert "> 报道范围：2026-07-27（Asia/Shanghai 自然日）" in summary
    assert "7月27日 01:00" in summary

    post_path = tmp_path / "docs" / "_posts" / "2026-07-28-summary-zh.md"
    post = post_path.read_text(encoding="utf-8")
    assert "content_date: 2026-07-27" in post
    assert "> 报道范围：2026-07-27（Asia/Shanghai 自然日）" in post

    audit_path = storage.audits_dir / "2026-07-28-candidate-audit.json"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    assert audit["state"] == "completed"
    assert audit["candidates"][0]["decision"] == "selected"


def test_save_candidate_audit_rejects_path_escape(tmp_path) -> None:
    storage = StorageManager(data_dir=str(tmp_path / "data"))

    with pytest.raises(ValueError, match="escapes intended root"):
        storage.save_candidate_audit("../../outside", {"safe": True})
