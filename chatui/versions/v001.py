import asyncio

from chatui.chat import Conversation


async def main() -> None:
    conversation = Conversation()
    while True:
        msg = input("Type your message: ")
        choices = await conversation.send(msg)
        print("Here are your choices:", choices)
        choice_index = input("Pick your choice: ")
        conversation.pick_response(choices[int(choice_index)])


if __name__ == "__main__":
    asyncio.run(main())
