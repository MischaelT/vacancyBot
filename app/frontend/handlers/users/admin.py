from aiogram import types

from frontend.handlers.users.start import bot_start
from frontend.keyboards.inline.admin_keyboard import admin_keyboard

from settings.backend_setup import backend_manager
from settings.config import ADMINS


async def show_admin_panel(message: types.Message):

    user_id = str(message.from_user.id)

    if user_id in ADMINS:
        markup = await admin_keyboard()
        text = 'Hello, admin'
        await message.answer(text=text, reply_markup=markup)
    else:
        await bot_start(message=message)
