from typing import Union

from aiogram import types

from frontend.keyboards.inline.back_keyboard import back_keyboard

from settings.config import backend_manager


async def get_vacancies(message: Union[types.Message, types.CallbackQuery]):

    user = backend_manager.user_data_manager.get_user(message.from_user.id)

    vacancies = await backend_manager.get_vacancies(user)
    markup = await back_keyboard(level=1)

    if isinstance(message, types.Message):
        for vacancy in vacancies:
            await message.answer(vacancy.to_print(), reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        result = ''

        for vacancy in vacancies:
            result += '\n' + f'{vacancy.to_print()}' + '\n'

        await call.message.edit_text(result, reply_markup=markup)
