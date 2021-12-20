from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


class Bot:
    def __init__(self) -> None:
        pass
        self.bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
        storage = MemoryStorage()
        self.dp = Dispatcher(self.bot, storage=storage)
