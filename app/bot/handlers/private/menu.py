from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram_dialog import DialogManager, StartMode

from app.bot.dialogs.main_dialog import MySG


async def on_menu_command(message: types.Message,
                          dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


def register_menu_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_menu_command, Command("menu"))
