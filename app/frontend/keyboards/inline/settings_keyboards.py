from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from frontend.data.buttons import SAVE_BUTTON
from frontend.data.consts import AREAS_LIST
from frontend.data.consts import Callbacks

menu_cd = CallbackData("show_menu", "level", "category")


def make_callback_data(level=0, category='0'):

    return menu_cd.new(level=level, category=category)


"""General settings keyboards"""


async def area_keyboard():

    """
    Function for generating experience keyoard

    Returns:
        markup: keyboard
    """

    markup = InlineKeyboardMarkup(row_width=3)

    categories = AREAS_LIST

    levels = [Callbacks.area_management.value,
              Callbacks.area_dev.value,
              Callbacks.area_ds.value,
              Callbacks.area_qa.value]

    for category, level in zip(categories, levels):

        button_text = f'{AREAS_LIST[category]}'
        callback_data = make_callback_data(level=level, category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


async def show_concrete_keyboard(keyboard_categories):

    markup = InlineKeyboardMarkup()

    for sub_category in keyboard_categories:

        if isinstance(keyboard_categories, dict):
            button_text = f'{keyboard_categories[sub_category]}'
        else:
            button_text = sub_category

        callback_data = make_callback_data(category=sub_category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


async def save_keyboard():

    """
    Function for generating save keyoard

    Returns:
        markup: keyboard
    """
    markup = InlineKeyboardMarkup()

    button_text = SAVE_BUTTON
    callback_data = make_callback_data(level=Callbacks.settings.value)

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    return markup
