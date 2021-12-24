from . import help  # noqa
from . import start  # noqa
from . import echo  # noqa

from .help import bot_help
from .start import bot_start
from .echo import bot_echo

from aiogram import Dispatcher

from aiogram.dispatcher.filters import CommandStart, CommandHelp



def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())
    dp.register_message_handler(bot_echo)
