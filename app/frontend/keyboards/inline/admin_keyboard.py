from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from frontend.data.consts import ADMIN_MENU_LIST, Callbacks

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

    categories = ADMIN_MENU_LIST

    levels = [Callbacks.run_parsing.value,
              Callbacks.get_users.value]

    for category, level in zip(categories, levels):

        button_text = f'{category}'
        callback_data = make_callback_data(level=level, category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup
