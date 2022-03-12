from typing import Union

from aiogram import types

from frontend.keyboards.inline.back_keyboard import back_keyboard

from settings.backend_setup import backend_manager


async def get_vacancies(message: Union[types.Message, types.CallbackQuery]):

    """
    Function for command /start

    Args:
        message (Union[types.Message, types.CallbackQuery]):  either Message or callback

    """

    user = backend_manager.user_data_manager.get_user(message.from_user.id)

    vacancies = backend_manager.vacancies_manager.get_data_by_filter(user)

    markup = await back_keyboard(level=1)
    

    if isinstance(message, types.Message):
        for vacancy in vacancies:
            await message.answer(vacancy.to_print(), reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):

        call = message
        reply_text = ''

        if len(vacancies) == 0:
            reply_text = 'There is no vacancies for you in database'
        else:
            for vacancy in vacancies:
                reply_text += '\n' + f'{vacancy.to_print()}' + '\n'

        await call.message.edit_text(reply_text, reply_markup=markup)
