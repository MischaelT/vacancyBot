from aiogram import types
from frontend.handlers.users.setUp_settings_handler import data_menu, developer_menu, experience_menu, management_menu, qa_menu, area_menu, save_menu

from frontend.handlers.users.main_handler import give_vacancies, main_menu, settings_menu, show_my_settings

 
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
        '11': management_menu,
        '12': data_menu,
        '13': qa_menu,
        '14': developer_menu,
        '15': save_menu,
    }

    current_level_func = levels[current_level]

    await current_level_func(call)