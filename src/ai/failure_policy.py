"""Safe retry and diagnostic helpers shared by AI pipeline stages.

The provider may attach full response bodies, prompts, or identifiers to its
exceptions.  These helpers deliberately retain only a small allowlist of
operational fields so they are safe to show in terminal output and audits.
"""

import random
import re
from typing import Optional

import httpx
from tenacity import RetryCallState, RetryError

from ..models import AIRequestFailureDiagnostic


_RETRYABLE_HTTP_STATUS_CODES = {408, 409, 429}
_SAFE_DIAGNOSTIC_TOKEN_RE = re.compile(r"^[A-Za-z0-9._:-]{1,128}$")
_SENSITIVE_DIAGNOSTIC_PREFIXES = (
    "sk-",
    "sk_",
    "aiza",
    "gsk_",
    "hf_",
    "xai-",
    "bearer",
)
_PROVIDER_ERROR_CATEGORIES = {
    "1301": "content_safety",
    "1302": "account_rate_limited",
    "1305": "provider_overloaded",
    "1308": "quota_exhausted",
    "1310": "quota_exhausted",
    "1313": "fair_use_limited",
}


def unwrap_retry_error(error: BaseException) -> tuple[BaseException, int]:
    """Return the final provider error and the caller-managed attempt count."""

    if not isinstance(error, RetryError):
        return error, 1

    last_attempt = error.last_attempt
    attempts = max(int(getattr(last_attempt, "attempt_number", 1)), 1)
    try:
        cause = last_attempt.exception()
    except BaseException:
        cause = None
    if isinstance(cause, BaseException):
        return cause, attempts
    return error, attempts


def http_status(error: BaseException) -> Optional[int]:
    """Read only a valid HTTP status code from a provider exception."""

    status = getattr(error, "status_code", None)
    if isinstance(status, bool) or not isinstance(status, int):
        return None
    return status if 100 <= status <= 599 else None


def safe_diagnostic_token(value: object) -> Optional[str]:
    """Keep a small allowlisted diagnostic token without response text."""

    if isinstance(value, bool) or not isinstance(value, (int, str)):
        return None
    token = str(value).strip()
    if token.lower().startswith(_SENSITIVE_DIAGNOSTIC_PREFIXES):
        return None
    if not _SAFE_DIAGNOSTIC_TOKEN_RE.fullmatch(token):
        return None
    return token


def provider_error_code(error: BaseException) -> Optional[str]:
    """Extract only a provider business code, never its message or body."""

    candidates = [getattr(error, "code", None)]
    body = getattr(error, "body", None)
    if isinstance(body, dict):
        candidates.append(body.get("code"))
        nested_error = body.get("error")
        if isinstance(nested_error, dict):
            candidates.append(nested_error.get("code"))
    for value in candidates:
        token = safe_diagnostic_token(value)
        if token is not None:
            return token
    return None


def provider_error_category(code: Optional[str]) -> Optional[str]:
    """Map documented provider codes to a stable, payload-free category."""

    if code is None:
        return None
    return _PROVIDER_ERROR_CATEGORIES.get(code)


def request_id(error: BaseException) -> Optional[str]:
    """Extract a safe request identifier when the provider exposed one."""

    for attribute in ("request_id", "_request_id"):
        token = safe_diagnostic_token(getattr(error, attribute, None))
        if token is not None:
            return token
    return None


def retry_after_seconds(error: BaseException) -> Optional[float]:
    """Read a bounded numeric Retry-After value without retaining headers."""

    response = getattr(error, "response", None)
    headers = getattr(response, "headers", None)
    if headers is None:
        return None

    for header_name, multiplier in (("retry-after-ms", 0.001), ("retry-after", 1.0)):
        try:
            raw_value = headers.get(header_name)
            seconds = float(raw_value) * multiplier
        except (AttributeError, TypeError, ValueError):
            continue
        if 0 < seconds <= 60:
            return seconds
    return None


def is_retryable_ai_exception(error: BaseException) -> bool:
    """Retry only transient transport and documented retryable HTTP failures."""

    root_error, _ = unwrap_retry_error(error)
    status = http_status(root_error)
    if status in _RETRYABLE_HTTP_STATUS_CODES:
        return True
    if status is not None and status >= 500:
        return True
    if isinstance(
        root_error,
        (
            ConnectionError,
            TimeoutError,
            httpx.NetworkError,
            httpx.TimeoutException,
        ),
    ):
        return True
    return type(root_error).__name__ in {
        "APIConnectionError",
        "APITimeoutError",
    }


def ai_retry_wait(retry_state: RetryCallState) -> float:
    """Use code-aware, jittered waits for provider rate limits and failures."""

    error = (
        retry_state.outcome.exception()
        if retry_state.outcome is not None
        else None
    )
    root_error, _ = unwrap_retry_error(error) if error else (Exception(), 1)
    retry_after = retry_after_seconds(root_error)
    if retry_after is not None:
        return retry_after

    code = provider_error_code(root_error)
    if code == "1302":
        # Account-level rate limit: let the provider's rolling window recover.
        base_delay, max_delay = 30.0, 60.0
    elif code == "1305":
        # Platform overload: back off, but do not assume the account is capped.
        base_delay, max_delay = 15.0, 60.0
    elif http_status(root_error) == 429:
        base_delay, max_delay = 10.0, 60.0
    else:
        base_delay, max_delay = 2.0, 20.0
    delay = min(base_delay * (2 ** (retry_state.attempt_number - 1)), max_delay)
    return min(max_delay, delay * random.uniform(0.75, 1.25))


def build_failure_diagnostic(error: BaseException) -> AIRequestFailureDiagnostic:
    """Create an audit-safe description of the final failed AI request."""

    root_error, attempts = unwrap_retry_error(error)
    code = provider_error_code(root_error)
    return AIRequestFailureDiagnostic(
        error_type=type(root_error).__name__,
        attempts=attempts,
        retryable=is_retryable_ai_exception(root_error),
        http_status=http_status(root_error),
        provider_error_code=code,
        provider_error_category=provider_error_category(code),
        request_id=request_id(root_error),
    )


def format_failure(
    diagnostic: AIRequestFailureDiagnostic,
    *,
    operation: str,
) -> str:
    """Render safe diagnostic fields for the terminal without provider payloads."""

    details = [diagnostic.error_type, f"attempts={diagnostic.attempts}"]
    if diagnostic.http_status is not None:
        details.append(f"status={diagnostic.http_status}")
    if diagnostic.provider_error_code is not None:
        details.append(f"code={diagnostic.provider_error_code}")
    if diagnostic.provider_error_category is not None:
        details.append(f"category={diagnostic.provider_error_category}")
    if diagnostic.request_id is not None:
        details.append(f"request_id={diagnostic.request_id}")
    return operation + " failed (" + "; ".join(details) + ")"
