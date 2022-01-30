from logging import makeLogRecord
from aiogram.types.inline_keyboard import InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup

menu_cd = CallbackData("show_menu", "level")

def make_callback_data(level):
    
    return menu_cd.new(level=level)
    
async def menu_keyboard():

    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup() 
    buttons = ['get vacancies', 'settings']

    for button in buttons:
        button_text = f'{button}'
        callback_data = make_callback_data(level=CURRENT_LEVEL)

        markup.insert(
            InlineKeyboardMarkup(text=button_text, callback_data=callback_data)
        )

    return markup