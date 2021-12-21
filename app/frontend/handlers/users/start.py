from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from app.main import bot

dp = bot.dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
