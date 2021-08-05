from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ParseMode
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.text import Jinja


class AnimalsSG(StatesGroup):
    animals = State()


async def get_data(**kwargs):
    return {
        "title": "Animals",
        "animals": ["cat", "dog", "fox"]
    }


html_text = Jinja("""
<b>{{title}}</b>
{% for animal in animals %}
* <a href="https://yandex.ru/search/?text={{ animal }}">{{ animal|capitalize }}</a>
{% endfor %}
""")

animals_window = Window(
    html_text,
    state=AnimalsSG.animals,
    getter=get_data
)

animals_dialog = Dialog(animals_window)
