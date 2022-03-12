from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext
from frontend.data.dialogs import CITY_DIALOG, EXPERIENCE_DIALOGS, LANGUAGE_DIALOG, MAIN_MENU_DIALOGS, SALARY_DIALOG, SETTINGS_DIALOGS
from frontend.data.consts import EXPERIENCES_LIST, LANGUAGE_LIST, SETTINGS_MENU

from settings.backend_setup import backend_manager

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

    """
    Main menu handler

    Args:
        message (Union[types.Message, types.CallbackQuery]): either Message or Callback
    """

    markup = await main_keyboard()

    if isinstance(message, types.Message):
        await message.answer(MAIN_MENU_DIALOGS[0] + message.from_user.full_name+ '\n' + "Let's find a job for you", reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_text(text=MAIN_MENU_DIALOGS[1], reply_markup=markup)


async def give_vacancies(message: types.Message, **kwargs):

    """
    Handler for giving vacancies for user

    Args:
        message (types.Message): message from user
    """    

    await get_vacancies(message)


async def settings_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):

    """
    Handler for giving settings menu

    Args:
        message (Union[types.Message, types.CallbackQuery]): either Message or Callback
    """

    markup = await settings_keyboard()

    if isinstance(message, types.Message):
        await message.answer(SETTINGS_DIALOGS[0], reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):

        call = message
        await call.message.edit_text(text=SETTINGS_DIALOGS[1], reply_markup=markup)


async def experience_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):

    """
    Handler for asking experience

    Args:
        message (Union[types.Message, types.CallbackQuery]):  either Message or Callback
    """  

    markup = await experience_keyboard()

    if isinstance(message, types.Message):
        await message.answer(EXPERIENCE_DIALOGS[0], reply_markup=markup)  # noqa
        await User_settings.experience.set()

    elif isinstance(message, types.CallbackQuery):

        call = message
        await call.message.edit_text(text=EXPERIENCE_DIALOGS[1], reply_markup=markup)
        await User_settings.experience.set()


async def language_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking language

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    experience = message.data.split(':')[2]

    async with state.proxy() as data:
        data["experience"] = experience

    markup = await language_keyboard()

    call = message
    await call.message.edit_text(text=LANGUAGE_DIALOG, reply_markup=markup)
    await User_settings.language.set()


async def city_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking user's city

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    language = message.data.split(':')[2]

    async with state.proxy() as data:
        data["language"] = language

    markup = await city_keyboard()

    call = message
    await call.message.edit_text(text=CITY_DIALOG, reply_markup=markup)
    await User_settings.city.set()


async def salary_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking desired salary

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    city = message.data.split(':')[2]

    async with state.proxy() as data:
        data["city"] = city

    markup = await salary_keyboard()

    call = message
    await call.message.edit_text(text=SALARY_DIALOG, reply_markup=markup)
    await User_settings.salary.set()


async def save_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking if the information correct

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    salary = message.data.split(':')[2]

    async with state.proxy() as data:
        city = data["city"]
        language = data["language"]
        experience = data['experience']

        data["salary"] = salary

    text = f'Your experience: {experience}, your language: {language}'+'\n'+f'your salary: {salary}, '+f'your city: {city}'+'\n'+'Save?'

    markup = await save_keyboard()

    call = message
    await call.message.edit_text(text=text, reply_markup=markup)

    await User_settings.save.set()
   

async def save_process(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Function for saving user's data

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    async with state.proxy() as data:
        city = data["city"]
        language = data["language"]
        experience = data['experience']
        salary = data['salary']

    user = backend_manager.user_data_manager.get_user(message.from_user.id)

    user.city = city
    user.experience = EXPERIENCES_LIST[experience]
    user.language = LANGUAGE_LIST[language]
    user.salary = salary

    backend_manager.user_data_manager.set_user(user)

    await state.reset_state()
    await settings_menu(message)


async def show_my_settings(message: types.CallbackQuery, **kwargs):

    """
    Function for shoving user's settings

    Args:
        message (types.Callback):  Callback
    """

    user_id = message.from_user.id
    user = backend_manager.user_data_manager.get_user(user_id=user_id)
    markup = await back_keyboard(level=SETTINGS_MENU)

    call = message
    await call.message.edit_text(text=f'{user.to_print()}', reply_markup=markup)


async def structure(call: types.CallbackQuery, callback_data: dict):

    """
    Callbacs structure 

    Args:
        message (types.Callback):  Callback
    """

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
