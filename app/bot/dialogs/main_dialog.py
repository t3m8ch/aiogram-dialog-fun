from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const


class MySG(StatesGroup):
    main = State()


main_window = Window(
    Const("Hello, %username%!"),
    Button(Const("Useless button"), id="nothing"),
    state=MySG.main
)

main_dialog = Dialog(main_window)
