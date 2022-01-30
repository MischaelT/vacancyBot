from aiogram.types.callback_query import CallbackQuery

from frontend.handlers.users.main_menu_handler import show_main_menu
from . import help  # noqa
from . import start  # noqa
from . import echo  # noqa

from .help import bot_help
from .start import bot_start
from .echo import bot_echo
from .settings_handler import ask_for_settings, navigate
from frontend.keyboards.inline.settings_keyboards import menu_cd

from aiogram import Dispatcher

from aiogram.dispatcher.filters import CommandStart, CommandHelp

def setup(dp: Dispatcher):

    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())
    dp.register_message_handler(ask_for_settings, commands=['settings'])
    dp.register_message_handler(show_main_menu, commands=['menu'])
    dp.register_callback_query_handler(navigate, menu_cd.filter())
