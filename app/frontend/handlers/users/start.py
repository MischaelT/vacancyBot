from aiogram import types

from frontend.handlers.users.main_handler import experience_menu
from frontend.keyboards.default.main_keyboard import main_keyboard

from settings.config import is_registered


async def bot_start(message: types.Message):

    if is_registered:
        await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=main_keyboard)

    else:
        await experience_menu(message, first_time=True)
