from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from frontend.data import config


class VacancyBot:
    def __init__(self) -> None:

        self.bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
        storage = MemoryStorage()
        self.dp = Dispatcher(self.bot, storage=storage)
