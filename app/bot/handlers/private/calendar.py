from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram_dialog import DialogManager, StartMode

from app.bot.dialogs.calendar_dialog import CalendarSG


async def on_date_command(message: types.Message,
                          dialog_manager: DialogManager):
    await dialog_manager.start(CalendarSG.calendar,
                               mode=StartMode.RESET_STACK)


def register_calendar_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_date_command, Command("date"))
