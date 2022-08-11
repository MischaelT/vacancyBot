from aiogram import types

from frontend.handlers.dialogs.main_handler import main_menu
from frontend.handlers.dialogs.setUp_settings_handler import area_menu

from settings.backend_setup import backend_manager


async def bot_start(message: types.Message):

    """
    Function for command /start

    Args:
        message (types.Message):  Message from user

    """

    user_id = message.from_user.id
    user = backend_manager.user_data_manager.get_user(user_id)

    if user.is_registered:
        await main_menu(message=message)
    else:
        await area_menu(message)
