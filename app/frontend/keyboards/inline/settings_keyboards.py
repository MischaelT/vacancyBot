from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

menu_cd = CallbackData("show_menu", "level", "category")
 

def make_callback_data(level=0, category='0'):

    return menu_cd.new(level=level, category=category)


async def settings_keyboard():

    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()

    categories = ['My settings', 'Change settings']

    button_text = f'{categories[0]}'
    callback_data = make_callback_data(level=7, category=categories[0])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    button_text = f'{categories[1]}'
    callback_data = make_callback_data(level=CURRENT_LEVEL+1, category=categories[1])    

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


async def back_keyboard(level):
    
    markup = InlineKeyboardMarkup()
    sub_categories = ['Back']

    for category in sub_categories:

        button_text = f'{category}'
        callback_data = make_callback_data(level=level, category=category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup