from aiogram import types

from backend.backend_manager import Backend_manager
from backend.user import User


async def get_vacancies(message: types.Message):

    user  = User('','','','')

    backend = Backend_manager(user)

    vacancies = await backend.get_latest_vacanvies()

    for vacancy in vacancies:
        await message.answer(vacancy.to_print())
    user  = User('','','','')