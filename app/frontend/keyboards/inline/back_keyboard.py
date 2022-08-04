from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from frontend.data.consts import BACK_BUTTON

menu_cd = CallbackData("show_menu", "level", "category")


def make_callback_data(level=0, category='0'):

    return menu_cd.new(level=level, category=category)


async def back_keyboard(level: int):

    """
    Keyboard with back button

    Args:
        level(int): level for going back
    """

    markup = InlineKeyboardMarkup()

    button_text = BACK_BUTTON
    callback_data = make_callback_data(level=level)

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    return markup
