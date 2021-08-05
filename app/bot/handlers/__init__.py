from aiogram import Dispatcher

from app.bot.handlers.private.animals import register_animals_handlers
from app.bot.handlers.private.help import register_help_handlers
from app.bot.handlers.private.menu import register_menu_handlers
from app.bot.handlers.private.start import register_start_handlers


def register_handlers(dispatcher: Dispatcher):
    register_animals_handlers(dispatcher)
    register_menu_handlers(dispatcher)
    register_start_handlers(dispatcher)
    register_help_handlers(dispatcher)
