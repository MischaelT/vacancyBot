from typing import Union

from aiogram import types

from frontend.data.consts import Callbacks
from frontend.data.dialogs import LETS_FIND_JOB, MAIN_MENU_DIALOGS, SETTINGS_DIALOGS
from frontend.handlers.users.get_vacancies import get_vacancies
from frontend.keyboards.inline.back_keyboard import back_keyboard
from frontend.keyboards.inline.main_keyboard import (main_keyboard,
                                                     settings_keyboard)

from settings.backend_setup import backend_manager


async def main_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):

    """
    Main menu handler

    Args:
        message (Union[types.Message, types.CallbackQuery]): either Message or Callback
    """

    markup = await main_keyboard()

    if isinstance(message, types.Message):

        text = f"{MAIN_MENU_DIALOGS[0]} {message.from_user.full_name}\
                \n{LETS_FIND_JOB}"

        await message.answer(text, reply_markup=markup)

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


async def show_my_settings(message: types.CallbackQuery, **kwargs):

    """
    Function for shoving user's settings

    Args:
        message (types.Callback):  Callback
    """

    user_id = message.from_user.id
    user = backend_manager.user_data_manager.get_user(user_id=user_id)
    markup = await back_keyboard(level=Callbacks.settings.value)

    call = message
    await call.message.edit_text(text=f'{user.to_print()}', reply_markup=markup)
