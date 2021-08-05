from aiogram import Dispatcher
from aiogram_dialog import DialogRegistry

from .menu_dialog import menu_dialog
from .animals_dialog import animals_dialog
from .scrolling_dialog import scrolling_dialog

__all__ = ["register_dialogs"]


def register_dialogs(dispatcher: Dispatcher):
    registry = DialogRegistry(dispatcher)
    registry.register(menu_dialog)
    registry.register(animals_dialog)
    registry.register(scrolling_dialog)
