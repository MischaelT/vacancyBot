from typing import Union

from aiogram.dispatcher import FSMContext

from aiogram import types
from frontend.utils.states.settings_states import User_settings

from frontend.keyboards.inline.settings_keyboards import back_keyboard, experience_keyboard, language_keyboard,\
                                                         save_keyboard, settings_keyboard


async def main_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):
    pass


async def settings_menu(message: Union[types.Message, types.CallbackQuery], first_time = False, **kwargs):

    markup = await settings_keyboard()

    if isinstance(message, types.Message):
        await message.answer('Lets change your settings', reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def experience_menu(message: types.CallbackQuery, **kwargs):

    markup = await experience_keyboard()

    call = message
    await call.message.edit_text(text = 'Please, choose your experience' ,reply_markup =markup)
    await User_settings.experience.set()


async def language_menu(message: types.CallbackQuery, state:FSMContext, **kwargs):

    experience = message.data.split(':')[2]

    async with state.proxy() as data:  # Работаем с данными из ФСМ
        data["experience"] = experience

    markup = await language_keyboard()

    call = message
    await call.message.edit_text(text = 'Please choose your language', reply_markup=markup)
    await User_settings.save.set()


async def save_menu(message: types.CallbackQuery, state:FSMContext, **kwargs):

    language = message.data.split(':')[2]

    async with state.proxy() as data:  # Работаем с данными из ФСМ

        experience = data['experience']

    text = f'Your experience: {experience}, your language: {language}. Save?'

    markup = await save_keyboard()

    call = message
    await call.message.edit_text(text = text, reply_markup=markup)

    await state.reset_state()

async def show_my_settings(message: types.CallbackQuery, **kwargs):


    message.data
    markup = await back_keyboard(level=1)

    call = message
    await call.message.edit_text(text = 'your settings', reply_markup=markup)


async def navigate(call: types.CallbackQuery, callback_data: dict):

    current_level = callback_data.get('level')

    levels = {
        '1': settings_menu,
        '2': experience_menu,
        # '3': language_menu,
        # '4': save_menu,
        '7': show_my_settings
    }
    current_level_func = levels[current_level]

    await current_level_func(call)
