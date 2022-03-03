from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandHelp, CommandStart

from frontend.handlers.users.vacancies import get_vacancies
from frontend.keyboards.inline.settings_keyboards import menu_cd

from .help import bot_help
from .settings_handler import ask_for_settings, navigate
from .start import bot_start


def setup(dp: Dispatcher):

    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())
    dp.register_message_handler(ask_for_settings, commands=['settings'])
    dp.register_message_handler(get_vacancies, commands=['vacancies'])
    # dp.register_message_handler(show_main_menu, commands=['menu'])
    dp.register_callback_query_handler(navigate, menu_cd.filter())
