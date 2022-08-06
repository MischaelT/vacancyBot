from aiogram import types

from frontend.handlers.users.main_handler import (give_vacancies, main_menu,
                                                  settings_menu,
                                                  show_my_settings)
from frontend.handlers.users.setUp_settings_handler import area_menu


async def dialog_structure(call: types.CallbackQuery, callback_data: dict):

    """
    Callbacs structure

    Args:
        message (types.Callback):  Callback
    """

    current_level = callback_data.get('level')

    levels = {
        '1': main_menu,
        '2': give_vacancies,
        '3': settings_menu,
        '4': show_my_settings,
        '10': area_menu,

    }

    current_level_func = levels[current_level]

    await current_level_func(call)
