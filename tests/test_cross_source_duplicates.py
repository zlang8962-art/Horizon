from datetime import datetime, timezone
from types import SimpleNamespace

from src.models import ContentItem, SourceType
from src.orchestrator import HorizonOrchestrator


NOW = datetime(2026, 1, 1, tzinfo=timezone.utc)


def item(
    item_id: str,
    url: str,
    *,
    source_type: SourceType = SourceType.RSS,
    title: str | None = None,
    content: str | None = None,
    metadata: dict | None = None,
) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=source_type,
        title=title or item_id,
        url=url,
        content=content,
        published_at=NOW,
        metadata=metadata or {},
    )


def merge(items: list[ContentItem]) -> list[ContentItem]:
    orchestrator = object.__new__(HorizonOrchestrator)
    return orchestrator.merge_cross_source_duplicates(items)


def compact(
    items: list[ContentItem],
    *,
    enabled: bool = True,
):
    orchestrator = object.__new__(HorizonOrchestrator)
    orchestrator.config = SimpleNamespace(
        filtering=SimpleNamespace(pre_analysis_title_dedup_enabled=enabled)
    )
    return orchestrator.compact_pre_analysis_candidates(items)


def test_normalizes_host_case_default_ports_path_trailing_slash_and_fragment() -> None:
    items = [
        item("one", "https://EXAMPLE.com:443/story/#first"),
        item("two", "https://example.com/story#second", source_type=SourceType.REDDIT),
    ]

    result = merge(items)

    assert len(result) == 1
    assert result[0].metadata["merged_sources"] == ["rss", "reddit"]


def test_preserves_scheme_and_non_default_port_distinctions() -> None:
    items = [
        item("https", "https://example.com/story"),
        item("http", "http://example.com/story"),
        item("custom-port", "https://example.com:8443/story"),
    ]

    result = merge(items)

    assert [merged.id for merged in result] == ["https", "http", "custom-port"]


def test_preserves_meaningful_query_parameters_and_their_order() -> None:
    items = [
        item("page-one", "https://example.com/story?page=1&sort=new"),
        item("page-two", "https://example.com/story?page=2&sort=new"),
        item("reordered", "https://example.com/story?sort=new&page=1"),
    ]

    result = merge(items)

    assert [merged.id for merged in result] == ["page-one", "page-two", "reordered"]


def test_removes_only_common_tracking_parameters() -> None:
    items = [
        item(
            "tracked",
            "https://example.com/story?id=42&utm_source=newsletter&fbclid=abc&GCLID=xyz",
        ),
        item("clean", "https://example.com/story?id=42", source_type=SourceType.REDDIT),
        item("meaningful", "https://example.com/story?id=42&source=newsletter"),
    ]

    result = merge(items)

    assert len(result) == 2
    assert result[0].metadata["merged_sources"] == ["rss", "reddit"]
    assert result[1].id == "meaningful"


def test_merge_preserves_richest_content_and_combines_metadata() -> None:
    items = [
        item("short", "https://example.com/story", content="short", metadata={"score": 12}),
        item(
            "rich",
            "https://example.com/story/",
            source_type=SourceType.REDDIT,
            content="the richer primary content",
            metadata={"comments": 4},
        ),
    ]

    result = merge(items)

    assert len(result) == 1
    assert result[0].id == "rich"
    assert result[0].content == "the richer primary content\n\n--- From rss ---\nshort"
    assert result[0].metadata == {
        "comments": 4,
        "score": 12,
        "merged_sources": ["rss", "reddit"],
    }


def test_returns_deep_copies_without_mutation_and_is_idempotent() -> None:
    singleton = item("single", "https://single.example/item", metadata={"nested": {"value": 1}})
    duplicate = item(
        "duplicate",
        "https://example.com/item",
        content="duplicate content",
        metadata={"nested": {"value": 2}},
    )
    primary = item(
        "primary",
        "https://example.com/item/",
        source_type=SourceType.REDDIT,
        content="primary content is longer",
        metadata={"discussion": {"count": 3}},
    )
    inputs = [singleton, duplicate, primary]
    before = [original.model_dump() for original in inputs]

    first = merge(inputs)
    first_before = [merged.model_dump() for merged in first]
    second = merge(first)

    assert [original.model_dump() for original in inputs] == before
    assert [merged.model_dump() for merged in first] == first_before
    assert second == first
    assert first[0] is not singleton
    assert first[0].metadata is not singleton.metadata
    assert first[0].metadata["nested"] is not singleton.metadata["nested"]
    assert first[1] is not primary
    assert first[1].metadata["nested"] is not duplicate.metadata["nested"]


def test_pre_analysis_compaction_keeps_one_google_news_headline_variant() -> None:
    first = item(
        "reuters",
        "https://news.example/reuters",
        source_type=SourceType.GOOGLE_NEWS,
        title="CXMT Announces New DRAM - Reuters",
        content="brief",
        metadata={"source_name": "Reuters"},
    )
    richest = item(
        "bloomberg",
        "https://news.example/bloomberg",
        source_type=SourceType.GOOGLE_NEWS,
        title="cxmt\u3000announces new dram — Bloomberg",
        content="the longer representative summary",
        metadata={"source_name": "Bloomberg"},
    )
    unrelated_source = item(
        "rss",
        "https://blog.example/cxmt",
        source_type=SourceType.RSS,
        title="CXMT Announces New DRAM - Reuters",
        content="independent source",
    )
    inputs = [first, richest, unrelated_source]
    before = [original.model_dump() for original in inputs]

    result = compact(inputs)

    assert [candidate.id for candidate in result.items] == ["bloomberg", "rss"]
    assert result.items[0].content == "the longer representative summary"
    assert result.enabled is True
    assert result.strategy == "google_news_exact_headline"
    assert result.excluded_duplicate_of == {"reuters": "bloomberg"}
    assert result.cluster_sizes == {"bloomberg": 2}
    assert [original.model_dump() for original in inputs] == before
    assert result.items[0] is not richest


def test_pre_analysis_compaction_is_off_by_default() -> None:
    first = item(
        "one",
        "https://news.example/one",
        source_type=SourceType.GOOGLE_NEWS,
        title="Same headline - One",
        metadata={"source_name": "One"},
    )
    second = item(
        "two",
        "https://news.example/two",
        source_type=SourceType.GOOGLE_NEWS,
        title="Same headline - Two",
        metadata={"source_name": "Two"},
    )
    inputs = [first, second]

    result = compact(inputs, enabled=False)

    assert result.items is inputs
    assert result.enabled is False
    assert result.strategy == "disabled"
    assert result.excluded_duplicate_of == {}


def test_pre_analysis_compaction_does_not_fuzzy_merge_headlines() -> None:
    confirmed = item(
        "confirmed",
        "https://news.example/confirmed",
        source_type=SourceType.GOOGLE_NEWS,
        title="CXMT opens new DRAM fab - Reuters",
        metadata={"source_name": "Reuters"},
    )
    speculation = item(
        "speculation",
        "https://news.example/speculation",
        source_type=SourceType.GOOGLE_NEWS,
        title="CXMT may open new DRAM fab - Bloomberg",
        metadata={"source_name": "Bloomberg"},
    )

    result = compact([confirmed, speculation])

    assert [candidate.id for candidate in result.items] == [
        "confirmed",
        "speculation",
    ]
    assert result.excluded_duplicate_of == {}
