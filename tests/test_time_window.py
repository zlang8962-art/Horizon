from datetime import datetime, timezone
from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from src.models import ContentItem, FilteringConfig, SourceType
from src.orchestrator import HorizonOrchestrator


def make_orchestrator(filtering: FilteringConfig) -> HorizonOrchestrator:
    orchestrator = HorizonOrchestrator.__new__(HorizonOrchestrator)
    orchestrator.config = SimpleNamespace(filtering=filtering)
    return orchestrator


def make_item(item_id: str, published_at: datetime) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=item_id,
        url=f"https://example.com/{item_id}",
        published_at=published_at,
    )


def test_previous_calendar_day_uses_configured_timezone() -> None:
    orchestrator = make_orchestrator(
        FilteringConfig(
            time_window_mode="previous_calendar_day",
            time_window_timezone="Asia/Shanghai",
        )
    )

    window = orchestrator._determine_time_window(
        now=datetime(2026, 7, 28, 7, 29, tzinfo=timezone.utc)
    )

    assert window.mode == "previous_calendar_day"
    assert window.report_date == "2026-07-28"
    assert window.content_date == "2026-07-27"
    assert window.since == datetime(2026, 7, 26, 16, 0, tzinfo=timezone.utc)
    assert window.until == datetime(2026, 7, 27, 16, 0, tzinfo=timezone.utc)


def test_force_hours_explicitly_overrides_calendar_mode() -> None:
    orchestrator = make_orchestrator(
        FilteringConfig(
            time_window_mode="previous_calendar_day",
            time_window_timezone="Asia/Shanghai",
        )
    )
    now = datetime(2026, 7, 28, 7, 29, tzinfo=timezone.utc)

    window = orchestrator._determine_time_window(force_hours=24, now=now)

    assert window.mode == "rolling_hours"
    assert window.content_date is None
    assert window.report_date == "2026-07-28"
    assert window.since == datetime(2026, 7, 27, 7, 29, tzinfo=timezone.utc)
    assert window.until == now


def test_calendar_window_includes_start_and_excludes_end() -> None:
    orchestrator = make_orchestrator(
        FilteringConfig(
            time_window_mode="previous_calendar_day",
            time_window_timezone="Asia/Shanghai",
        )
    )
    window = orchestrator._determine_time_window(
        now=datetime(2026, 7, 28, 7, 29, tzinfo=timezone.utc)
    )
    items = [
        make_item("before", datetime(2026, 7, 26, 15, 59, 59, tzinfo=timezone.utc)),
        make_item("start", window.since),
        make_item("inside", datetime(2026, 7, 27, 8, 0, tzinfo=timezone.utc)),
        make_item("end", window.until),
    ]

    kept = orchestrator._filter_items_to_window(items, window)

    assert [item.id for item in kept] == ["start", "inside"]


def test_invalid_time_window_timezone_is_rejected() -> None:
    with pytest.raises(ValidationError, match="valid IANA timezone"):
        FilteringConfig(time_window_timezone="Not/A-Timezone")
