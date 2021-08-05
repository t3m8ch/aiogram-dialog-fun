import logging
import random

from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery
from aiogram_dialog import Window, Dialog, DialogManager, ChatEvent
from aiogram_dialog.widgets.kbd import Button, Group, Checkbox, Radio, Select
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
        "color": "red",
        "languages": ["RU", "EN", "DE"]
    }


async def on_random_name(call: types.CallbackQuery,
                         button: Button,
                         manager: DialogManager):
    await call.message.answer(random.choice((
        "Artem", "Mikhail", "Olga", "Maria"
    )))


async def on_random_number(call: types.CallbackQuery,
                           button: Button,
                           manager: DialogManager):
    await call.message.answer(str(random.randint(1, 100)))


async def on_check_state_change(event: ChatEvent, checkbox: Checkbox,
                                manager: DialogManager):
    logging.debug(
        "-"*30 + f" Check status changed: {checkbox.is_checked(manager)}"
    )


async def on_language_selected(call: CallbackQuery, select: Select,
                               manager: DialogManager, item: str):
    await call.message.answer(f"Вы выбрали: {item}")


menu_window = Window(
    Format("Hello, {name}"),
    Group(
        Button(Const("Useless button"), id="nothing"),
        Button(Const("Random name"), id="randname", on_click=on_random_name),
        Button(Const("Random number"), id="randnum", on_click=on_random_number),
        width=2
    ),
    Checkbox(
        Const("✅ On"),
        Const("❌ Off"),
        id="check",
        default=True,
        on_state_changed=on_check_state_change
    ),
    Radio(
        Format("🔘 {item}"),
        Format("⚪️ {item}"),
        id="r_languages",
        item_id_getter=lambda item: item,
        items="languages",
        on_state_changed=on_language_selected,
    ),
    color_text,
    state=MySG.main,
    getter=get_data
)

menu_dialog = Dialog(menu_window)
