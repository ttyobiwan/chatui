import openai

from chatui import settings

openai.api_key = settings.OPENAI_KEY


class Conversation:
    """ChatGPT conversation manager."""

    model: str = "gpt-3.5-turbo"

    def __init__(self) -> None:
        self.messages: list[dict] = []

    async def send(self, message: str) -> list[str]:
        """Send a message to the chat and return choices."""
        self.messages.append({"role": "user", "content": message})
        r = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=self.messages,
        )
        return [choice["message"]["content"] for choice in r["choices"]]  # type: ignore

    def pick_response(self, choice: str) -> None:
        """Pick a single response from the choices."""
        self.messages.append({"role": "assistant", "content": choice})

    def clear(self) -> None:
        """Clear current conversation."""
        self.messages = []
