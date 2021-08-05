import random

from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format, Case


class MySG(StatesGroup):
    main = State()


color_text = Case(
    {
        "red": Const("Square"),
        "green": Const("Unicorn"),
        "blue": Const("Moon"),
    },
    selector="color"
)


async def get_data(**kwargs):
    return {
        "name": "T3M8CH",
        "color": "red"
    }


async def on_random_name(call: types.CallbackQuery,
                         button: Button,
                         manager: DialogManager):
    await call.message.answer(random.choice((
        "Artem", "Mikhail", "Olga", "Maria"
    )))


menu_window = Window(
    Format("Hello, {name}"),
    Button(Const("Useless button"), id="nothing"),
    Button(Const("Random name"), id="randname", on_click=on_random_name),
    color_text,
    state=MySG.main,
    getter=get_data
)

menu_dialog = Dialog(menu_window)
