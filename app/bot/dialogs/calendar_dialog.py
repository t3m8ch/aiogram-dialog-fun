from datetime import date

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Window, Dialog
from aiogram_dialog.widgets.kbd import Calendar
from aiogram_dialog.widgets.text import Const


class CalendarSG(StatesGroup):
    calendar = State()


async def on_date_selected(call: CallbackQuery, widget,
                           manager: DialogManager, selected_date: date):
    await call.message.edit_text(str(selected_date))


calendar_window = Window(
    Const("Calendar"),
    Calendar(id='calendar', on_click=on_date_selected),
    state=CalendarSG.calendar
)

calendar_dialog = Dialog(calendar_window)
