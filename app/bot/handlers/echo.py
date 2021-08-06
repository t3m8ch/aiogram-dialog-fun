from aiogram import types, Dispatcher


async def echo(message: types.Message):
    if message.entities:
        await message.answer(", ".join(str(e) for e in message.entities))
    await message.answer(message.text)


def register_echo_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(echo)
