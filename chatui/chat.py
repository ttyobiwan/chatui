import openai

from chatui import settings

openai.api_key = settings.OPENAI_KEY


class Conversation:
    model: str = "gpt-3.5-turbo"

    def __init__(self) -> None:
        self.messages: list[dict] = []

    async def send(self, message: str) -> list[str]:
        self.messages.append({"role": "user", "content": message})
        r = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=self.messages,
        )
        return [choice["message"]["content"] for choice in r["choices"]]  # type: ignore

    def pick_response(self, choice: str) -> None:
        self.messages.append({"role": "assistant", "content": choice})
