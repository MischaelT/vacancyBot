from typing import Union
from aiogram import types

from frontend.keyboards.inline.categories_menu import settings_keyboard

async def ask_for_settings(message: types.Message):
    await list_settings(message=message)

async def list_settings(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = settings_keyboard()
