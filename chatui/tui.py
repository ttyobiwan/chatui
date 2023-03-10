from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widget import Widget
from textual.widgets import Button, Header, Input, Static

from chatui.chat import Conversation


class MessageBox(Widget):
    def __init__(self, text: str, role: str) -> None:
        self.text = text
        self.role = role
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(self.text, classes=f"message {self.role}")


class ChatApp(App):
    TITLE = "chatui"
    SUB_TITLE = "ChatGPT directly in your terminal"

    CSS_PATH = "static/styles.css"

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(id="conversation_box")
        yield Horizontal(
            Input(placeholder="Enter your message", id="message_input"),
            Button(label="Send", variant="success", id="send_button"),
            id="input_box",
        )

    def on_mount(self) -> None:
        self.conversation = Conversation()
        self.query_one(Input).focus()

    async def on_button_pressed(self) -> None:
        await self.process_conversation()

    async def on_input_submitted(self) -> None:
        await self.process_conversation()

    async def process_conversation(self) -> None:
        message_input = self.query_one("#message_input")
        button = self.query_one("#send_button")
        conversation_box = self.query_one("#conversation_box")

        self.toggle_widgets(message_input, button)

        # Create question message, add it to the conversation and scroll down
        message_box = MessageBox(message_input.value, "question")
        conversation_box.mount(message_box)
        conversation_box.scroll_end(animate=False)

        # Clean up the input without triggering events
        with message_input.prevent(Input.Changed):
            message_input.value = ""

        # Take answer from the chat and add it to the conversation
        choices = await self.conversation.send(message_box.text)
        self.conversation.pick_response(choices[0])
        conversation_box.mount(
            MessageBox(
                choices[0].removeprefix("\n").removeprefix("\n"),
                "answer",
            )
        )

        self.toggle_widgets(message_input, button)
        # Single scroll doesn't work - don't ask me why
        conversation_box.scroll_end(animate=False)
        conversation_box.scroll_end(animate=False)

    def toggle_widgets(self, *widgets: Widget) -> None:
        for w in widgets:
            w.disabled = not w.disabled
