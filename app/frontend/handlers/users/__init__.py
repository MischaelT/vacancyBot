from concurrent.futures import process
from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from frontend.utils.states.settings_states import User_settings

from frontend.handlers.users.vacancies import get_vacancies
from frontend.keyboards.inline.settings_keyboards import menu_cd

from .help import bot_help
from .main_handler import language_menu, navigate, save_menu, settings_menu
from .start import bot_start


def setup(dp: Dispatcher):

    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())

    dp.register_message_handler(get_vacancies, commands=['vacancies'])


    dp.register_message_handler(settings_menu, commands=['settings'], state=None)
    dp.register_callback_query_handler(language_menu, state=User_settings.experience)

    dp.register_callback_query_handler(save_menu, state=User_settings.save)

    dp.register_callback_query_handler(navigate, menu_cd.filter())


