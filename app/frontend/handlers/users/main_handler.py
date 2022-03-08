from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext
from frontend.data.consts import SETTINGS_MENU
from backend.models.user import User

from settings.config import backend_manager

from frontend.handlers.users.vacancies import get_vacancies
from frontend.keyboards.inline.main_keyboard import main_keyboard
from frontend.keyboards.inline.settings_keyboards import (city_keyboard,
                                                          experience_keyboard,
                                                          language_keyboard, salary_keyboard,
                                                          save_keyboard,
                                                          settings_keyboard)
                                                          
from frontend.keyboards.inline.back_keyboard import back_keyboard                                         
from frontend.utils.states.settings_states import User_settings


async def main_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):

    markup = await main_keyboard()

    print(type(message))

    if isinstance(message, types.Message):
        await message.answer('Welcome, ' +message.from_user.full_name+ '\n' + "Let's find a job for you", reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_text(text="Let's find a job for you", reply_markup=markup)


async def give_vacancies(message: types.Message, **kwargs):

    await get_vacancies(message)


async def settings_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):

    markup = await settings_keyboard()

    if isinstance(message, types.Message):
        await message.answer('Lets change your settings', reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):

        call = message
        await call.message.edit_text(text='Settings', reply_markup=markup)


async def experience_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):

    markup = await experience_keyboard()

    if isinstance(message, types.Message):
        await message.answer('Seems you are new to our system' + '\n' + 'Lets set up your settings'+'\n'+ 'Please enter your experience', reply_markup=markup)  # noqa
        await User_settings.experience.set()

    elif isinstance(message, types.CallbackQuery):

        call = message
        await call.message.edit_text(text='Please, choose your experience', reply_markup=markup)
        await User_settings.experience.set()


async def language_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    experience = message.data.split(':')[2]

    async with state.proxy() as data:
        data["experience"] = experience

    markup = await language_keyboard()

    call = message
    await call.message.edit_text(text='Please choose your language', reply_markup=markup)
    await User_settings.language.set()


async def city_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    language = message.data.split(':')[2]

    async with state.proxy() as data:
        data["language"] = language

    markup = await city_keyboard()

    call = message
    await call.message.edit_text(text='Please choose your city', reply_markup=markup)
    await User_settings.city.set()


async def salary_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    city = message.data.split(':')[2]

    async with state.proxy() as data:
        data["city"] = city

    markup = await salary_keyboard()

    call = message
    await call.message.edit_text(text='Please desired salary', reply_markup=markup)
    await User_settings.salary.set()


async def save_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):
    

    salary = message.data.split(':')[2]

    async with state.proxy() as data:
        city = data["city"]
        language = data["language"]
        experience = data['experience']

        data["salary"] = salary

    text = f'Your experience: {experience}, your language: {language}'+'\n'+f'your salary: {salary}'+f'your city: {city}'+'\n'+'Save?'

    markup = await save_keyboard()

    call = message
    await call.message.edit_text(text=text, reply_markup=markup)

    await User_settings.save.set()
   

async def save_process(message: types.CallbackQuery, state: FSMContext, **kwargs):

    async with state.proxy() as data:
        city = data["city"]
        language = data["language"]
        experience = data['experience']
        salary = data['salary']

    user = User(
                user_id = message.from_user.id,
                is_registered=True,
                experience=experience,
                city = city,
                language=language,
                salary=salary
    )

    backend_manager.user_data_manager.set_user(user)

    await state.reset_state()
    await settings_menu(message)

async def show_my_settings(message: types.CallbackQuery, **kwargs):

    message.data
    markup = await back_keyboard(level=SETTINGS_MENU)

    call = message
    await call.message.edit_text(text='your settings', reply_markup=markup)


async def navigate(call: types.CallbackQuery, callback_data: dict):

    current_level = callback_data.get('level')

    levels = {
        '1': main_menu,
        '2': give_vacancies,
        '3': settings_menu,
        '4': show_my_settings,
        '5': experience_menu,


    }

    current_level_func = levels[current_level]

    await current_level_func(call)
