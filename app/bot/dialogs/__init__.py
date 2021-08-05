from aiogram import Dispatcher
from aiogram_dialog import DialogRegistry

from .main_dialog import main_dialog

__all__ = ["register_dialogs"]


def register_dialogs(dispatcher: Dispatcher):
    registry = DialogRegistry(dispatcher)
    registry.register(main_dialog)
