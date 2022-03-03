from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

menu_cd = CallbackData("show_menu", "level", "category")


def make_callback_data(level, category='0'):

    return menu_cd.new(level=level, category=category)


async def settings_keyboard():
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()

    categories = ['my_settings', 'change_settings']

    for category in categories:
        button_text = f'{category}'
        callback_data = make_callback_data(level=CURRENT_LEVEL+1, category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


async def experience_keyboard():

    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup()
    sub_categories = ['Trainee', 'Junior', 'Middle', 'Senior', 'Architect']

    for category in sub_categories:

        button_text = f'{category}'
        callback_data = make_callback_data(level=CURRENT_LEVEL+1, category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )
    return markup


async def language_keyboard():

    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    sub_categories = ['Python', 'Java', 'C++', 'Scala']

    for category in sub_categories:

        button_text = f'{category}'
        callback_data = make_callback_data(level=CURRENT_LEVEL+1, category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


async def save_keyboard():
    CURRENT_LEVEL = 4
    markup = InlineKeyboardMarkup()
    sub_categories = ['Save']

    for category in sub_categories:

        button_text = f'{category}'
        callback_data = make_callback_data(level=CURRENT_LEVEL-3, category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup
