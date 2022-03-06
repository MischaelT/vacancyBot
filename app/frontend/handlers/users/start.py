import random
from aiogram import types
from app.frontend.handlers.users.main_handler import settings_menu

from frontend.keyboards.default.main_keyboard import main_keyboard


async def bot_start(message: types.Message):

    not_registered = bool(random.getrandbits(1))

    if not_registered:
        await settings_menu(message, first_time = True)
    else:
        await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=main_keyboard)
