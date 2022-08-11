from aiogram import types

from frontend.data.dialogs import ADMIN
from frontend.handlers.users.start import bot_start
from frontend.keyboards.inline.admin_keyboard import admin_keyboard

from settings.config import ADMINS


async def show_admin_panel(message: types.Message):

    user_id = str(message.from_user.id)

    if user_id in ADMINS:

        markup = await admin_keyboard()

        if isinstance(message, types.Message):
            await message.answer(ADMIN, reply_markup=markup)

        elif isinstance(message, types.CallbackQuery):
            call = message
            await call.message.edit_text(text=ADMIN, reply_markup=markup)
    else:
        await bot_start(message=message)
