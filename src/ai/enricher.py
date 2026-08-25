"""Content enrichment using AI (second-pass analysis).

For items that pass the score threshold, this module searches for context and
generates grounded background knowledge. It also keeps Chinese publication
quality explicit when a provider request cannot be completed.
"""

import asyncio
import os
import re
import sys
from typing import List, Optional

from ddgs import DDGS
from rich.progress import BarColumn, MofNCompleteColumn, Progress, SpinnerColumn, TextColumn
from tenacity import retry, retry_if_exception, stop_after_attempt

from .client import AIClient
from .failure_policy import (
    ai_retry_wait,
    build_failure_diagnostic,
    format_failure,
    is_retryable_ai_exception,
)
from .prompts import (
    CONCEPT_EXTRACTION_SYSTEM,
    CONCEPT_EXTRACTION_USER,
    CONTENT_ENRICHMENT_SYSTEM,
    CONTENT_ENRICHMENT_USER,
)
from .utils import parse_json_response
from ..models import AIEnrichmentFailureDiagnostic, ContentItem


_CJK_RE = re.compile(r"[\u3400-\u9fff]")


class InvalidEnrichmentResponseError(RuntimeError):
    """The model returned a response that did not meet the enrichment contract."""


class MissingChineseEnrichmentSummaryError(RuntimeError):
    """The enrichment response lacked a usable Simplified Chinese summary."""


class ContentEnricher:
    """Enriches high-scoring content items with background knowledge."""

    def __init__(self, ai_client: AIClient):
        self.client = ai_client

    def _get_concurrency(self) -> int:
        """Return the configured enrichment concurrency, clamped to 1 or above."""

        config = getattr(self.client, "config", None)
        concurrency = getattr(config, "enrichment_concurrency", 1)
        return max(concurrency, 1)

    async def enrich_batch(self, items: List[ContentItem]) -> None:
        """Enrich items in-place with background knowledge.

        Failures remain non-fatal for an otherwise selected digest item, but are
        always marked with a safe diagnostic and a Chinese-only fallback.
        """

        concurrency = self._get_concurrency()
        semaphore = asyncio.Semaphore(concurrency)

        async def _process(item: ContentItem, progress_task) -> None:
            async with semaphore:
                try:
                    await self._enrich_item(item)
                    if not self._has_chinese_summary(item):
                        raise MissingChineseEnrichmentSummaryError()
                    item.ai_enrichment_failure = None
                except Exception as error:
                    await self._recover_enrichment_failure(item, error)
            progress.advance(progress_task)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            transient=True,
        ) as progress:
            task = progress.add_task("Enriching", total=len(items))
            coros = [_process(item, task) for item in items]
            await asyncio.gather(*coros)

    async def _recover_enrichment_failure(
        self,
        item: ContentItem,
        error: BaseException,
    ) -> None:
        """Apply a safe fallback without logging provider bodies or prompts."""

        base_diagnostic = build_failure_diagnostic(error)
        if base_diagnostic.provider_error_category == "content_safety":
            # The provider says its content filter matched. Do not immediately
            # re-submit the same title/summary to a second model call.
            fallback = "content_safety_notice"
            self._apply_chinese_notice(item)
        else:
            translated = await self._translate_item(item)
            fallback = "translated" if translated else "zh_notice"
            if not translated:
                self._apply_chinese_notice(item)

        diagnostic = AIEnrichmentFailureDiagnostic(
            **base_diagnostic.model_dump(),
            stage="enrichment",
            fallback=fallback,
        )
        item.ai_enrichment_failure = diagnostic
        message = format_failure(diagnostic, operation="AI enrichment")
        print(f"Error enriching item {item.id}: {message}; fallback={fallback}")

    async def _web_search(self, query: str, max_results: int = 3) -> list:
        """Search the web for context via DuckDuckGo."""

        try:
            # Suppress primp "Impersonate ... does not exist" stderr warning.
            stderr = sys.stderr
            sys.stderr = open(os.devnull, "w")
            try:
                ddgs = DDGS()
                results = await asyncio.to_thread(ddgs.text, query, max_results=max_results)
            finally:
                sys.stderr.close()
                sys.stderr = stderr
        except Exception:
            return []

        return [
            {"title": r.get("title", ""), "url": r.get("href", ""), "body": r.get("body", "")}
            for r in (results or [])
        ]

    @staticmethod
    def _parse_json_response(response: str) -> Optional[dict]:
        """Try multiple strategies to extract a JSON object from an AI response."""

        return parse_json_response(response)

    async def _complete_for_enrichment(self, *, system: str, user: str) -> str:
        """Call the client with caller-managed retries when it supports them."""

        complete = getattr(self.client, "complete_for_retrying_caller", None)
        if callable(complete):
            return await complete(system=system, user=user)
        return await self.client.complete(system=system, user=user)

    async def _extract_concepts(self, item: ContentItem, content_text: str) -> List[str]:
        """Ask AI to identify concepts that may need explanation.

        This optional planning call intentionally does not retry itself. The
        main enrichment request owns the bounded retry policy, while a missed
        concept query simply means enrichment proceeds without web context.
        """

        user_prompt = CONCEPT_EXTRACTION_USER.format(
            title=item.title,
            summary=item.ai_summary or item.title,
            tags=", ".join(item.ai_tags) if item.ai_tags else "",
            content=content_text[:1000],
        )

        try:
            response = await self._complete_for_enrichment(
                system=CONCEPT_EXTRACTION_SYSTEM,
                user=user_prompt,
            )
            result = self._parse_json_response(response)
            if result is None:
                return []
            queries = result.get("queries", [])
            return queries[:3] if isinstance(queries, list) else []
        except Exception:
            return []

    @retry(
        retry=retry_if_exception(is_retryable_ai_exception),
        stop=stop_after_attempt(3),
        wait=ai_retry_wait,
    )
    async def _enrich_item(self, item: ContentItem) -> None:
        """Enrich a single item with background knowledge."""

        content_text = ""
        comments_text = ""
        if item.content:
            if "--- Top Comments ---" in item.content:
                main, comments_part = item.content.split("--- Top Comments ---", 1)
                content_text = main.strip()[:4000]
                comments_text = comments_part.strip()[:2000]
            else:
                content_text = item.content[:4000]

        queries = await self._extract_concepts(item, content_text)

        all_results = []
        web_sections = []
        for query in queries:
            results = await self._web_search(query)
            all_results.extend(results)
            if results:
                lines = [f"- [{r['title']}]({r['url']}): {r['body']}" for r in results]
                web_sections.append(f"**{query}:**\n" + "\n".join(lines))
        web_context = "\n\n".join(web_sections) if web_sections else ""

        available_urls = {r["url"]: r["title"] for r in all_results if r.get("url")}
        user_prompt = CONTENT_ENRICHMENT_USER.format(
            title=item.title,
            url=str(item.url),
            summary=item.ai_summary or item.title,
            score=item.ai_score or 0,
            reason=item.ai_reason or "",
            tags=", ".join(item.ai_tags) if item.ai_tags else "",
            content=content_text,
            comments_section=f"\n**Community Comments:**\n{comments_text}" if comments_text else "",
            web_context=web_context or "No web search results available.",
        )
        response = await self._complete_for_enrichment(
            system=CONTENT_ENRICHMENT_SYSTEM,
            user=user_prompt,
        )
        result = self._parse_json_response(response)
        if result is None:
            raise InvalidEnrichmentResponseError()

        for lang in ("en", "zh"):
            title = self._text_value(result.get(f"title_{lang}"))
            if title:
                item.metadata[f"title_{lang}"] = title

            parts = [
                text
                for field in ("whats_new", "why_it_matters", "key_details")
                if (text := self._text_value(result.get(f"{field}_{lang}")))
            ]
            if parts:
                item.metadata[f"detailed_summary_{lang}"] = " ".join(parts)

            background = self._text_value(result.get(f"background_{lang}"))
            if background:
                item.metadata[f"background_{lang}"] = background

            discussion = self._text_value(result.get(f"community_discussion_{lang}"))
            if discussion:
                item.metadata[f"community_discussion_{lang}"] = discussion

        if result.get("sources") and available_urls and isinstance(result["sources"], list):
            valid = [
                {"url": url, "title": available_urls[url]}
                for url in result["sources"]
                if isinstance(url, str) and url in available_urls
            ]
            if valid:
                item.metadata["sources"] = valid

        self._suppress_non_chinese_zh_fields(item)
        item.metadata["detailed_summary"] = item.metadata.get("detailed_summary_en", "")
        item.metadata["background"] = item.metadata.get("background_en", "")
        item.metadata["community_discussion"] = item.metadata.get("community_discussion_en", "")

    @retry(
        retry=retry_if_exception(is_retryable_ai_exception),
        stop=stop_after_attempt(3),
        wait=ai_retry_wait,
    )
    async def _request_translation(self, item: ContentItem) -> str:
        """Request a bounded, caller-managed Chinese translation fallback."""

        return await self._complete_for_enrichment(
            system="You are a translator. Translate to Simplified Chinese. Return only valid JSON, no other text.",
            user=(
                f"Title: {item.title}\n"
                f"Summary: {item.ai_summary or item.title}\n\n"
                "Return JSON:\n"
                '{"title_zh": "<中文标题>", "summary_zh": "<用中文写1-2句摘要>"}'
            ),
        )

    async def _translate_item(self, item: ContentItem) -> bool:
        """Try a Chinese-only fallback and report whether it is usable."""

        try:
            response = await self._request_translation(item)
        except Exception:
            return False

        result = self._parse_json_response(response)
        if result is None:
            return False

        summary = self._text_value(result.get("summary_zh"))
        if not self._contains_chinese(summary):
            return False

        title = self._text_value(result.get("title_zh"))
        if self._contains_chinese(title):
            item.metadata["title_zh"] = title
        item.metadata["detailed_summary_zh"] = summary
        # A fallback supplies only a short Chinese summary. Do not later fall
        # through to stale English background/discussion fields in the renderer.
        item.metadata["zh_output_incomplete"] = True
        return True

    @staticmethod
    def _text_value(value: object) -> str:
        """Accept only plain, non-empty text from the untrusted model response."""

        if isinstance(value, dict):
            value = value.get("text")
        return value.strip() if isinstance(value, str) else ""

    @staticmethod
    def _contains_chinese(value: object) -> bool:
        return isinstance(value, str) and bool(_CJK_RE.search(value))

    def _has_chinese_summary(self, item: ContentItem) -> bool:
        return self._contains_chinese(item.metadata.get("detailed_summary_zh"))

    def _suppress_non_chinese_zh_fields(self, item: ContentItem) -> None:
        """Prevent an English value in a `_zh` field from leaking to Chinese output."""

        incomplete = False
        for key in (
            "title_zh",
            "detailed_summary_zh",
            "background_zh",
            "community_discussion_zh",
        ):
            value = item.metadata.get(key)
            if isinstance(value, str) and value and not self._contains_chinese(value):
                item.metadata.pop(key, None)
                incomplete = True
        if incomplete:
            item.metadata["zh_output_incomplete"] = True

    @staticmethod
    def _apply_chinese_notice(item: ContentItem) -> None:
        """Use a transparent Chinese notice rather than silently publishing English."""

        item.metadata["detailed_summary_zh"] = (
            "该条资讯的中文内容暂不可用；请查看原文链接获取详情。"
        )
        item.metadata.pop("background_zh", None)
        item.metadata.pop("community_discussion_zh", None)
        item.metadata["zh_output_incomplete"] = True
