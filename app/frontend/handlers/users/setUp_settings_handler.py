import logging
from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from backend.data.db.choices import DATA, DEVELOPMENT, MANAGEMENT, TEST

from frontend.data.consts import AREAS_LIST, EXPERIENCES_LIST, LANGUAGE_LIST
from frontend.data.dialogs import (AREA_DIALOGS, DATA_DIALOG, DEVELOPER_DIALOG,
                                   EXPERIENCE_DIALOGS, LANGUAGE_DIALOG,
                                   LOCATION_DIALOG, MANAGEMENT_DIALOG,
                                   QA_DIALOG, SALARY_DIALOG)
from frontend.handlers.users.main_handler import settings_menu
from frontend.keyboards.inline.settings_keyboards import (area_keyboard,
                                                          city_keyboard,
                                                          data_keyboard,
                                                          developer_keyboard,
                                                          experience_keyboard,
                                                          language_keyboard,
                                                          management_keyboard,
                                                          qa_keyboard,
                                                          salary_keyboard,
                                                          save_keyboard)
from frontend.utils.states.settings_states import UserSettings

from settings.backend_setup import backend_manager

"""GENERAL SETTINGS METHODS"""


async def area_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):

    """
    Handler for giving settings menu

    Args:
        message (Union[types.Message, types.CallbackQuery]): either Message or Callback
    """

    logging.debug(message)

    markup = await area_keyboard()

    if isinstance(message, types.Message):
        await message.answer(AREA_DIALOGS[0], reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_text(text=AREA_DIALOGS[1], reply_markup=markup)

    await UserSettings.experience.set()


async def experience_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking experience

    Args:
        message (Union[types.Message, types.CallbackQuery]):  either Message or Callback
    """

    area = message.data.split(':')[2]

    markup = await experience_keyboard()

    call = message
    await call.message.edit_text(text=EXPERIENCE_DIALOGS, reply_markup=markup)

    if area == MANAGEMENT:
        await UserSettings.management.set()
    elif area == DATA:
        await UserSettings.data.set()
    elif area == TEST:
        await UserSettings.qa.set()
    elif area == DEVELOPMENT:
        await UserSettings.developer.set()

"""DEVELOPERS SETTINGS METHODS"""


async def developer_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking language

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    experience = message.data.split(':')[2]

    async with state.proxy() as data:
        data["area"] = DEVELOPMENT
        data["experience"] = experience

    markup = await developer_keyboard()

    call = message
    await call.message.edit_text(text=DEVELOPER_DIALOG, reply_markup=markup)
    await UserSettings.language.set()

"""QA SETTINGS METHODS"""


async def qa_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking language

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    experience = message.data.split(':')[2]

    async with state.proxy() as data:
        data["experience"] = experience
        data["area"] = TEST

    markup = await qa_keyboard()

    call = message
    await call.message.edit_text(text=QA_DIALOG, reply_markup=markup)
    await UserSettings.language.set()

"""DATA SETTINGS METHODS"""


async def data_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking language

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """
    experience = message.data.split(':')[2]

    async with state.proxy() as data:
        data["experience"] = experience
        data["area"] = DATA

    markup = await data_keyboard()

    call = message
    await call.message.edit_text(text=DATA_DIALOG, reply_markup=markup)
    await UserSettings.language.set()


"""MANAGEMENT SETTINGS METHODS"""


async def management_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking language

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    experience = message.data.split(':')[2]

    async with state.proxy() as data:
        data["experience"] = experience
        data["area"] = MANAGEMENT

    markup = await management_keyboard()

    call = message
    await call.message.edit_text(text=MANAGEMENT_DIALOG, reply_markup=markup)
    await UserSettings.salary.set()


async def language_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking language

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    position = message.data.split(':')[2]

    async with state.proxy() as data:
        data["position"] = position

    markup = await language_keyboard()

    call = message
    await call.message.edit_text(text=LANGUAGE_DIALOG, reply_markup=markup)
    await UserSettings.salary.set()


async def salary_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking desired salary

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    async with state.proxy() as data:
        area = data["area"]

    if area == MANAGEMENT:

        position = message.data.split(':')[2]

        async with state.proxy() as data:
            data["position"] = position

    else:

        language = message.data.split(':')[2]

        async with state.proxy() as data:
            data["language"] = language

    markup = await salary_keyboard()

    call = message
    await call.message.edit_text(text=SALARY_DIALOG, reply_markup=markup)
    await UserSettings.location.set()


async def location_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking user's city

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    salary = message.data.split(':')[2]

    async with state.proxy() as data:
        data["salary"] = salary

    markup = await city_keyboard()

    call = message
    await call.message.edit_text(text=LOCATION_DIALOG, reply_markup=markup)
    await UserSettings.save.set()


"""SERVICE METHODS"""


async def save_menu(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Handler for asking if the information correct

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    location = message.data.split(':')[2]

    async with state.proxy() as data:
        data["location"] = location

    async with state.proxy() as data:
        salary = data["salary"]
        experience = data['experience']
        area = data['area']
        position = data['position']

    if area == MANAGEMENT:

        text = f"Your area: {AREAS_LIST[area]},\
        \nSpecialisation: {position}\
        \nExperience: {experience}\
        \nLocation: {location}\
        \nSalary: {salary}\
        \nSave?"

    else:
        async with state.proxy() as data:

            language = LANGUAGE_LIST[data["language"]]
            text = f"Your area: {AREAS_LIST[area]}\
            \nSpecialisation: {position}\
            \nLanguage: {language}\
            \nExperience: {experience}\
            \nLocation: {location}\
            \nSalary: {salary}\
            \nSave?"

    markup = await save_keyboard()

    call = message
    await call.message.edit_text(text=text, reply_markup=markup)

    await UserSettings.save_process.set()


async def save_process(message: types.CallbackQuery, state: FSMContext, **kwargs):

    """
    Function for saving user's data

    Args:
        message (types.Callback):  Callback
        state (FSMContext): FSMState for current handler
    """

    async with state.proxy() as data:
        location = data["location"]
        salary = data["salary"]
        experience = data['experience']
        area = data['area']
        position = data['position']

    user = backend_manager.user_data_manager.get_user(message.from_user.id)

    user.area = area

    if area == DEVELOPMENT:
        language = data['language']
        user.language = language
        user.position = position
    elif area == TEST:
        language = data['language']
        user.language = language
        user.position = position
    elif area == DATA:
        language = data['language']
        user.language = language
        user.position = position
    else:
        user.language = 'language'
        user.position = position

    user.experience = EXPERIENCES_LIST[experience]

    user.location = location
    user.salary = salary

    backend_manager.user_data_manager.set_user(user)

    await state.reset_state()
    await settings_menu(message)
