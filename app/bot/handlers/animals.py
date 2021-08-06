from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram_dialog import DialogManager, StartMode

from app.bot.dialogs.animals_dialog import AnimalsSG


async def on_animals_command(message: types.Message,
                             dialog_manager: DialogManager):
    await dialog_manager.start(AnimalsSG.animals, mode=StartMode.RESET_STACK)


def register_animals_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_animals_command, Command("animals"))
