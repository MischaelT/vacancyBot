from aiogram import types

from frontend.keyboards.default.main_keyboard import main_keyboard


async def bot_start(message: types.Message):

    await message.answer(f"Привет, {message.from_user.full_name}!. Жми /menu", reply_markup=main_keyboard)
