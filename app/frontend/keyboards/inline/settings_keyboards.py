from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from frontend.data.consts import (AREA_DEVELOPER, AREA_DS, AREA_MANAGEMENT, AREA_QA, AREAS_LIST, CITIES_LIST, DATA_OPTIONS,
                                  DEVELOPER_OPTIONS, EXPERIENCES_LIST, LANGUAGE_LIST,
                                  MANAGEMENT_OPTIONS, QA_OPTIONS, SALARIES_LIST,
                                  SAVE_BUTTON, SETTINGS_MENU)

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

    categories = list(AREAS_LIST.keys())

    button_text = f'{AREAS_LIST[categories[0]]}'
    callback_data = make_callback_data(level=AREA_MANAGEMENT, category=categories[0])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    button_text = f'{AREAS_LIST[categories[1]]}'
    callback_data = make_callback_data(level=AREA_DS, category=categories[1])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    button_text = f'{AREAS_LIST[categories[2]]}'
    callback_data = make_callback_data(level=AREA_DEVELOPER, category=categories[2])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    button_text = f'{AREAS_LIST[categories[3]]}'
    callback_data = make_callback_data(level=AREA_QA, category=categories[3])

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )
    return markup

async def experience_keyboard():

    """
    Function for generating experience keyoard

    Returns:
        markup: keyboard
    """

    markup = InlineKeyboardMarkup()
    categories = EXPERIENCES_LIST

    for sub_category in categories:

        button_text = f'{categories[sub_category]}'
        callback_data = make_callback_data(category=sub_category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup

async def city_keyboard():

    """
    Function for generating city keyoard

    Returns:
        markup: keyboard
    """

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

    """
    Function for generating salary keyoard

    Returns:
        markup: keyboard
    """

    markup = InlineKeyboardMarkup()
    categories = SALARIES_LIST

    for sub_category in categories:

        button_text = f'{sub_category}'
        callback_data = make_callback_data(category=sub_category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup

"""DEVELOPERS SETTINGS KEYBOARDS"""

async def developer_keyboard():

    """
    Function for generating language keyoard

    Returns:
        markup: keyboard
    """

    markup = InlineKeyboardMarkup()
    categories = DEVELOPER_OPTIONS

    for sub_category in categories:

        button_text = f'{sub_category}'
        callback_data = make_callback_data(category=sub_category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup

async def language_keyboard():

    """
    Function for generating language keyoard

    Returns:
        markup: keyboard
    """

    markup = InlineKeyboardMarkup()
    categories = LANGUAGE_LIST

    for sub_category in categories:

        button_text = f'{categories[sub_category]}'
        callback_data = make_callback_data(category=sub_category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


"""QA SETTINGS KEYBOARDS"""

async def qa_keyboard():

    """
    Function for generating language keyoard

    Returns:
        markup: keyboard
    """

    markup = InlineKeyboardMarkup()
    categories = QA_OPTIONS

    for sub_category in categories:

        button_text = f'{sub_category}'
        callback_data = make_callback_data(category=sub_category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup

"""MANAGEMENT SETTINGS KEYBOARDS"""

async def management_keyboard():

    """
    Function for generating language keyoard

    Returns:
        markup: keyboard
    """

    markup = InlineKeyboardMarkup()
    categories = MANAGEMENT_OPTIONS

    for sub_category in categories:

        button_text = f'{sub_category}'
        callback_data = make_callback_data(category=sub_category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup

"""MANAGEMENT SETTINGS KEYBOARDS"""

async def data_keyboard():

    """
    Function for generating language keyoard

    Returns:
        markup: keyboard
    """

    markup = InlineKeyboardMarkup()
    categories = DATA_OPTIONS

    for sub_category in categories:

        button_text = f'{sub_category}'
        callback_data = make_callback_data(category=sub_category)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup


"""Service Keyboards"""

async def save_keyboard():

    """
    Function for generating save keyoard

    Returns:
        markup: keyboard
    """
    markup = InlineKeyboardMarkup()

    button_text = SAVE_BUTTON
    callback_data = make_callback_data(level=SETTINGS_MENU)

    markup.insert(
        InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
    )

    return markup