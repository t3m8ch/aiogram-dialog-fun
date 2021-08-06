from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram_dialog import DialogManager, StartMode

from app.bot.dialogs.scrolling_dialog import ScrollingSG


async def on_scrolling_command(message: types.Message,
                               dialog_manager: DialogManager):
    await dialog_manager.start(ScrollingSG.scrolling,
                               mode=StartMode.RESET_STACK)


def register_scrolling_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_scrolling_command,
                                        Command("scrolling"))
