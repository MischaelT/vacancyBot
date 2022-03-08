from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandHelp, CommandStart

from frontend.handlers.users.vacancies import get_vacancies
from frontend.keyboards.inline.settings_keyboards import menu_cd
from frontend.utils.states.settings_states import User_settings

from .help import bot_help
from .main_handler import city_menu, language_menu, navigate, salary_menu, save_menu, save_process, settings_menu
from .start import bot_start


def setup(dp: Dispatcher):

    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())

    dp.register_message_handler(get_vacancies, commands=['vacancies'])
    dp.register_message_handler(settings_menu, commands=['settings'], state=None)

    dp.register_callback_query_handler(language_menu, state=User_settings.experience)
    dp.register_callback_query_handler(city_menu, state=User_settings.language)
    dp.register_callback_query_handler(salary_menu, state=User_settings.city)
    dp.register_callback_query_handler(save_menu, state=User_settings.salary)    
    dp.register_callback_query_handler(save_process, state=User_settings.save)

    dp.register_callback_query_handler(navigate, menu_cd.filter())
