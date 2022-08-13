from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from frontend.data.consts import (MAIN_MENU_LIST, SETTINGS_MENU_LIST)
from frontend.data.buttons import BACK_BUTTON
from frontend.data.consts import Callbacks

menu_cd = CallbackData("show_menu", "level", "category")


def make_callback_data(level=0, category='0'):

    return menu_cd.new(level=level, category=category)


async def main_keyboard():

    """
    Function for generating main menu keyoard

    Returns:
    markup(keyboard): main keyboard

    """

    markup = InlineKeyboardMarkup()

    categories = MAIN_MENU_LIST

    levels = [Callbacks.get_vacancies.value,
              Callbacks.settings.value]

    for category, level in zip(categories, levels):

        button_text = f'{category}'
        callback_data = make_callback_data(level=level, category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


async def settings_keyboard():

    """
    Function for generating main menu keyoard

    Returns:
        markup: settings keyboard
    """

    markup = InlineKeyboardMarkup(row_width=2)

    categories = SETTINGS_MENU_LIST
    categories.append(BACK_BUTTON)

    levels = [Callbacks.my_settings.value,
              Callbacks.choose_area.value,
              Callbacks.main.value]

    for category, level in zip(categories, levels):

        button_text = f'{category}'
        callback_data = make_callback_data(level=level, category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup
