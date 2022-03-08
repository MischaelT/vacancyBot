from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from frontend.data.consts import CITIES_LIST, EXPERIENCES_LIST, LANGUAGE_LIST, MAIN_MENU, MY_SETTINGS, SALARIES_LIST, SAVE_BUTTON, SET_SETTINGS, SETTINGS_MENU, SETTINGS_MENU_LIST

menu_cd = CallbackData("show_menu", "level", "category")


def make_callback_data(level=0, category='0'):

    return menu_cd.new(level=level, category=category)


async def settings_keyboard():

    markup = InlineKeyboardMarkup(row_width=2)

    categories = SETTINGS_MENU_LIST

    button_text = f'{categories[0]}'
    callback_data = make_callback_data(level=MY_SETTINGS, category=categories[0])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    button_text = f'{categories[1]}'
    callback_data = make_callback_data(level=SET_SETTINGS, category=categories[1])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    button_text = f'{categories[2]}'
    callback_data = make_callback_data(level=MAIN_MENU, category=categories[2])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    return markup


async def experience_keyboard():

    markup = InlineKeyboardMarkup()
    sub_categories = EXPERIENCES_LIST

    for category in sub_categories:

        button_text = f'{category}'
        callback_data = make_callback_data(category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


async def language_keyboard():

    markup = InlineKeyboardMarkup()
    sub_categories = LANGUAGE_LIST

    for category in sub_categories:

        button_text = f'{category}'
        callback_data = make_callback_data(category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


async def city_keyboard():

    markup = InlineKeyboardMarkup()
    sub_categories = CITIES_LIST

    for category in sub_categories:

        button_text = f'{category}'
        callback_data = make_callback_data(category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


async def salary_keyboard():

    markup = InlineKeyboardMarkup()
    sub_categories = SALARIES_LIST

    for category in sub_categories:

        button_text = f'{category}'
        callback_data = make_callback_data(category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


async def save_keyboard():

    markup = InlineKeyboardMarkup()

    button_text = SAVE_BUTTON
    callback_data = make_callback_data(level=SETTINGS_MENU)

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    return markup
