from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


button_1 = KeyboardButton('/vacancies')
button_2 = KeyboardButton('/settings')

main_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
)


main_keyboard.row(button_1)
main_keyboard.row(button_2)
