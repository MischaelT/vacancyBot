import logging

from aiogram import types

from frontend.data.consts import Callbacks
from frontend.handlers.dialogs.main_handler import (give_vacancies, main_menu,
                                                    settings_menu,
                                                    show_my_settings)
from frontend.handlers.dialogs.setUp_settings_handler import area_menu
from frontend.handlers.users.admin import show_admin_panel
from frontend.handlers.users.get_users import get_users

from settings.backend_setup import backend_manager


async def dialog_structure(call: types.CallbackQuery, callback_data: dict):

    """
    Callbacs structure

    Args:
        message (types.Callback):  Callback
    """
    logging.debug('HERE')

    current_level = int(callback_data.get('level'))

    levels = {
        Callbacks.main.value: main_menu,
        Callbacks.get_vacancies.value: give_vacancies,
        Callbacks.settings.value: settings_menu,
        Callbacks.my_settings.value: show_my_settings,
        Callbacks.admin.value: show_admin_panel,
        Callbacks.run_parsing.value: backend_manager.run_async_parsing,
        Callbacks.get_users.value: get_users,
        Callbacks.choose_area.value: area_menu,
    }

    current_level_func = levels[current_level]

    await current_level_func(call)
