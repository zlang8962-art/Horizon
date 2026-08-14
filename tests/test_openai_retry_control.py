import asyncio
from types import SimpleNamespace

from src.ai.client import OpenAIClient


class _FakeCompletions:
    def __init__(self) -> None:
        self.requests: list[dict[str, object]] = []

    async def create(self, **kwargs):  # type: ignore[no-untyped-def]
        self.requests.append(kwargs)
        return SimpleNamespace(
            usage=None,
            choices=[SimpleNamespace(message=SimpleNamespace(content="{}"))],
        )


class _FakeOpenAITransport:
    def __init__(self) -> None:
        self.completions = _FakeCompletions()
        self.chat = SimpleNamespace(completions=self.completions)
        self.options: list[dict[str, object]] = []

    def with_options(self, **kwargs):  # type: ignore[no-untyped-def]
        self.options.append(kwargs)
        return self


def test_openai_analysis_calls_disable_sdk_retries() -> None:
    transport = _FakeOpenAITransport()
    client = OpenAIClient.__new__(OpenAIClient)
    client.client = transport
    client.config = SimpleNamespace(thinking="disabled")
    client.model = "glm-4.7-flash"
    client.temperature = 0.3
    client.max_tokens = 128
    client.provider = "zhipu"
    client._supports_temperature = True
    client._use_max_completion_tokens = False

    result = asyncio.run(
        client.complete_for_retrying_caller(
            system="Return JSON.",
            user="Test request.",
        )
    )

    assert result == "{}"
    assert transport.options == [{"max_retries": 0}]
    assert transport.completions.requests[0]["model"] == "glm-4.7-flash"
    assert transport.completions.requests[0]["extra_body"] == {
        "thinking": {"type": "disabled"}
    }
