from aiogram import types

from frontend.handlers.users.main_handler import experience_menu, main_menu

from settings.backend_setup import backend_manager


async def bot_start(message: types.Message):

    """
    Function for command /start

    Args:
        message (types.Message):  Message from user

    """

    user_id = message.from_user.id
    user = backend_manager.user_data_manager.get_user(user_id)

    await backend_manager.run_general_parsing()

    if user.is_registered:
        await main_menu(message=message)
    else:
        await experience_menu(message, first_time=True)
