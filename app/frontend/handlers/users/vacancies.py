from aiogram import types


async def get_vacancies(message: types.Message):

    await message.answer('vacancies')
