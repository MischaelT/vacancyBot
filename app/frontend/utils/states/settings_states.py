from aiogram.dispatcher.filters.state import StatesGroup, State

class User_settings(StatesGroup):
    experience = State()
    language = State()
    save = State()