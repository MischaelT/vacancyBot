from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

menu_cd = CallbackData("show_menu", "level", "category")


def make_callback_data(level=0, category='0'):

    return menu_cd.new(level=level, category=category)


async def main_keyboard():

    markup = InlineKeyboardMarkup()

    categories = ['Get vacancies', 'Settings']

    button_text = f'{categories[0]}'
    callback_data = make_callback_data(level=4, category=categories[0])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    button_text = f'{categories[1]}'
    callback_data = make_callback_data(level=1, category=categories[1])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    return markup
