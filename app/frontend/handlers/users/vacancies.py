from typing import Union

from aiogram import types

from frontend.keyboards.inline.settings_keyboards import back_keyboard

from settings.config import backend_manager

# from backend.user import User


async def get_vacancies(message: Union[types.Message, types.CallbackQuery]):

    # user = User('', '', '', '')

    vacancies = await backend_manager.get_latest_vacanvies()
    markup = await back_keyboard(level=3)

    if isinstance(message, types.Message):
        for vacancy in vacancies:
            await message.answer(vacancy.to_print(), reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        result = ''
        for vacancy in vacancies:
            result += '\n' + f'{vacancy.to_print()}' + '\n'
        await call.message.edit_text(result, reply_markup=markup)
