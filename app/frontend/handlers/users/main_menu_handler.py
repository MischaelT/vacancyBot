from typing import Union

from aiogram import types

from frontend.keyboards.inline.main_menu import menu_keyboard


async def show_main_menu(message: types.Message):
    await main_menu(message=message)


async def main_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):

    markup = await menu_keyboard()

    if isinstance(message, types.Message):
        await message.answer('оп', reply_markup=markup)

    # elif isinstance(message, types.CallbackQuery):
    #     call = message
    #     with suppress(MessageNotModified):
    #         await call.message.edit_reply_markup(markup)
