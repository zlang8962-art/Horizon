"""RSS feed scraper implementation."""

import calendar
import hashlib
import logging
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List, Literal, Optional
from email.utils import parsedate_to_datetime
import httpx
import feedparser

from .base import BaseScraper
from ..extractors import ExtractorRegistry
from ..models import ContentItem, SourceType, RSSSourceConfig

logger = logging.getLogger(__name__)

RSS_REQUEST_HEADERS = {
    "User-Agent": "Horizon/0.1 (+https://github.com/zlang8962-art/Horizon)",
    "Accept": "application/atom+xml, application/rss+xml, application/xml, text/xml, */*;q=0.1",
}


@dataclass(frozen=True)
class RSSFeedFetchOutcome:
    """Payload-free health result for one configured RSS feed."""

    source_name: str
    status: Literal["success", "empty", "failure"]
    item_count: int
    error_type: Optional[str] = None
    http_status: Optional[int] = None

    def to_dict(self) -> dict[str, object]:
        result: dict[str, object] = {
            "source": self.source_name,
            "status": self.status,
            "item_count": self.item_count,
        }
        if self.error_type is not None:
            result["error_type"] = self.error_type
        if self.http_status is not None:
            result["http_status"] = self.http_status
        return result


class RSSScraper(BaseScraper):
    """Scraper for RSS/Atom feeds."""

    def __init__(
        self,
        sources: List[RSSSourceConfig],
        http_client: httpx.AsyncClient,
        extractors: Optional[ExtractorRegistry] = None,
    ):
        """Initialize RSS scraper.

        Args:
            sources: List of RSS feed configurations
            http_client: Shared async HTTP client
            extractors: Optional registry of content extractors for full article fetching
        """
        super().__init__({"sources": sources}, http_client)
        self._extractors = extractors
        self.last_fetch_outcomes: List[RSSFeedFetchOutcome] = []

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch RSS feed items.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        items = []
        outcomes: List[RSSFeedFetchOutcome] = []
        sources = self.config["sources"]

        for source in sources:
            if not source.enabled:
                continue

            feed_items, outcome = await self._fetch_feed(source, since)
            items.extend(feed_items)
            outcomes.append(outcome)

        self.last_fetch_outcomes = outcomes
        return items

    async def _fetch_feed(
        self, source: RSSSourceConfig, since: datetime
    ) -> tuple[List[ContentItem], RSSFeedFetchOutcome]:
        """Fetch items from a single RSS feed.

        Args:
            source: RSS feed configuration
            since: Only fetch items after this time

        Returns:
            The feed items and a safe health outcome.
        """
        items = []

        try:
            # Expand environment variables in URL (e.g. ${LWN_TOKEN})
            feed_url = re.sub(
                r"\$\{(\w+)\}",
                lambda m: os.environ.get(m.group(1), m.group(0)).strip(),
                str(source.url),
            )

            # Fetch feed content
            response = await self.client.get(
                feed_url,
                follow_redirects=True,
                headers=RSS_REQUEST_HEADERS,
            )
            response.raise_for_status()

            # Parse feed
            feed = feedparser.parse(response.text)

            for entry in feed.entries:
                # Parse published date
                published_at = self._parse_date(entry)
                if not published_at or published_at < since:
                    continue

                # Generate unique ID from feed URL and entry ID
                feed_id = str(source.url).split("//")[1].replace("/", "_")
                entry_id = entry.get("id", entry.get("link", ""))
                entry_hash = hashlib.sha256(str(entry_id).encode("utf-8")).hexdigest()[
                    :16
                ]

                # Extract content
                content = self._extract_content(entry)

                if source.content_extractor and self._extractors:
                    extractor = self._extractors.get(source.content_extractor)
                    if extractor:
                        url = entry.get("link", "")
                        if url:
                            full = await extractor.extract(url, self.client)
                            if full:
                                content = full

                item = ContentItem(
                    id=self._generate_id("rss", feed_id, entry_hash),
                    source_type=SourceType.RSS,
                    title=entry.get("title", "Untitled"),
                    url=entry.get("link", str(source.url)),
                    content=content,
                    author=entry.get("author", source.name),
                    published_at=published_at,
                    metadata={
                        "feed_name": source.name,
                        "category": source.category,
                        "tags": [tag.term for tag in entry.get("tags", [])],
                    },
                )
                items.append(item)

        except httpx.HTTPError as error:
            response = getattr(error, "response", None)
            status = getattr(response, "status_code", None)
            if isinstance(status, bool) or not isinstance(status, int):
                status = None
            logger.warning(
                "RSS feed fetch failed source=%s type=%s status=%s",
                source.name,
                type(error).__name__,
                status,
            )
            return [], RSSFeedFetchOutcome(
                source_name=source.name,
                status="failure",
                item_count=0,
                error_type=type(error).__name__,
                http_status=status,
            )
        except Exception as error:
            logger.warning(
                "RSS feed processing failed source=%s type=%s",
                source.name,
                type(error).__name__,
            )
            return [], RSSFeedFetchOutcome(
                source_name=source.name,
                status="failure",
                item_count=0,
                error_type=type(error).__name__,
            )

        return items, RSSFeedFetchOutcome(
            source_name=source.name,
            status="success" if items else "empty",
            item_count=len(items),
        )

    def _parse_date(self, entry: dict) -> Optional[datetime]:
        """Parse publication date from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            datetime: Parsed publication date or None
        """
        # Try different date fields
        for field in ["published", "updated", "created"]:
            if field in entry:
                try:
                    # Try parsing structured time first
                    if f"{field}_parsed" in entry and entry[f"{field}_parsed"]:
                        return datetime.fromtimestamp(
                            calendar.timegm(entry[f"{field}_parsed"]), tz=timezone.utc
                        )
                    # Fallback to string parsing
                    date_str = str(entry[field]).strip()
                    if date_str.isdigit():
                        timestamp = int(date_str)
                        if timestamp >= 1_000_000_000_000:
                            timestamp /= 1000
                        return datetime.fromtimestamp(timestamp, tz=timezone.utc)
                    return parsedate_to_datetime(date_str)
                except Exception:
                    continue

        return None

    def _extract_content(self, entry: dict) -> str:
        """Extract text content from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            str: Extracted text content
        """
        # Try different content fields
        if "summary" in entry:
            return entry.summary
        if "description" in entry:
            return entry.description
        if "content" in entry and entry.content:
            # content is usually a list
            return entry.content[0].get("value", "")

        return ""
