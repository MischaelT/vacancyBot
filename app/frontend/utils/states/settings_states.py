from aiogram.dispatcher.filters.state import State, StatesGroup


class User_settings(StatesGroup):
    experience = State()
    language = State()
    city = State()
    save = State()
    salary = State()
