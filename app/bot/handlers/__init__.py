from aiogram import Dispatcher

from .animals import register_animals_handlers
from .calendar import register_calendar_handlers
from .echo import register_echo_handlers
from .help import register_help_handlers
from .menu import register_menu_handlers
from .scrolling import register_scrolling_handlers
from .start import register_start_handlers


def register_handlers(dispatcher: Dispatcher):
    register_animals_handlers(dispatcher)
    register_menu_handlers(dispatcher)
    register_scrolling_handlers(dispatcher)
    register_calendar_handlers(dispatcher)

    register_start_handlers(dispatcher)
    register_help_handlers(dispatcher)
    register_echo_handlers(dispatcher)
