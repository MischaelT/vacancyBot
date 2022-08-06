from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from frontend.data.consts import GET_VACANCIES_MENU

menu_cd = CallbackData("show_menu", "level", "category")


def make_callback_data(level=0, category='0'):

    return menu_cd.new(level=level, category=category)


async def admin_keyboard():

    """
    Function for generating main menu keyoard

    Returns:
    markup(keyboard): main keyboard

    """

    markup = InlineKeyboardMarkup()

    categories = ['Run parsing']

    button_text = f'{categories[0]}'
    callback_data = make_callback_data(level=GET_VACANCIES_MENU, category=categories[0])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )
    return markup
