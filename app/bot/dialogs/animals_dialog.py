from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog.widgets.text import Jinja, Format, Const


class AnimalsSG(StatesGroup):
    animals = State()
    selected = State()


async def get_data(**kwargs):
    return {
        "title": "Animals",
        "animals": ["cat", "dog", "fox"]
    }


async def on_animal_selected(call: CallbackQuery, select: Select,
                             manager: DialogManager, item: str):
    await manager.dialog().next(manager)


html_text = Jinja("""
<b>{{title}}</b>
{% for animal in animals %}
* <a href="https://yandex.ru/search/?text={{ animal }}">{{ animal|capitalize }}</a>
{% endfor %}
""")

animals_dialog = Dialog(
    Window(
        html_text,
        Select(
            Format("{item}"),
            id="select_animal",
            item_id_getter=lambda item: item,
            items="animals",
            on_click=on_animal_selected
        ),
        state=AnimalsSG.animals,
        getter=get_data
    ),
    Window(
        Const("Вы выбрали животное"),
        state=AnimalsSG.selected
    )
)
