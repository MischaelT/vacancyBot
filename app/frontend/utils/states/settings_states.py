from aiogram.dispatcher.filters.state import State, StatesGroup


class UserSettings(StatesGroup):

    """
    States for ask settings conversation

    """

    experience = State()
    language = State()
    location = State()
    area = State()
    developer = State()
    qa = State()
    management = State()
    data = State()
    specialisation = State()
    salary = State()
    save = State()
    save_process = State()