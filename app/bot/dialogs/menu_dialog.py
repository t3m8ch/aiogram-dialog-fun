from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_dialog import Window, Dialog
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


menu_window = Window(
    Format("Hello, {name}"),
    Button(Const("Useless button"), id="nothing"),
    color_text,
    state=MySG.main,
    getter=get_data
)

menu_dialog = Dialog(menu_window)
