from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button, ScrollingGroup
from aiogram_dialog.widgets.text import Const


class ScrollingSG(StatesGroup):
    scrolling = State()


scrolling_window = Window(
    Const("Scrolling"),
    ScrollingGroup(
        *(Button(Const(str(i)), id="i") for i in range(0, 99)),
        id="scrolling",
        width=6,
        height=6
    ),
    state=ScrollingSG.scrolling
)

scrolling_dialog = Dialog(scrolling_window)
