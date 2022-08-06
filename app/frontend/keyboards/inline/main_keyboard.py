from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from frontend.data.consts import (BACK_BUTTON, CHOOSE_AREA, GET_VACANCIES_MENU,
                                  MAIN_MENU, MY_SETTINGS, SETTINGS_MENU,
                                  SETTINGS_MENU_LIST)

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

    categories = ['Get vacancies', 'Settings']

    button_text = f'{categories[0]}'
    callback_data = make_callback_data(level=GET_VACANCIES_MENU, category=categories[0])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    button_text = f'{categories[1]}'
    callback_data = make_callback_data(level=SETTINGS_MENU, category=categories[1])

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

    button_text = f'{categories[0]}'
    callback_data = make_callback_data(level=MY_SETTINGS, category=categories[0])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    button_text = f'{categories[1]}'
    callback_data = make_callback_data(level=CHOOSE_AREA, category=categories[1])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    button_text = BACK_BUTTON
    callback_data = make_callback_data(level=MAIN_MENU)

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    return markup
