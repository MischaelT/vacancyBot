from aiogram import types

from frontend.data.dialogs import NO_USERS
from frontend.data.consts import Callbacks
from frontend.keyboards.inline.back_keyboard import back_keyboard

from settings.backend_setup import backend_manager


async def get_users(message: types.CallbackQuery):

    """
    Function for command /start

    Args:
        message (Union[types.Message, types.CallbackQuery]):  either Message or callback

    """

    users = backend_manager.user_data_manager.get_users()

    markup = await back_keyboard(level=Callbacks.admin.value)

    call = message

    reply_text = ''

    if not users:
        reply_text = NO_USERS
    else:
        for user in users:
            reply_text += '\n' + f'{user._id}' + '\n'

    await call.message.edit_text(reply_text, reply_markup=markup)
