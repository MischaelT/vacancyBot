import logging

from aiogram import Bot, Dispatcher, executor, types
# from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from settings.config import BOT_TOKEN
# , REDIS_HOST, REDIS_PASSWORD, REDIS_PORT

from frontend import handlers, middlewares
from frontend.utils.notify_admins import on_startup_notify
from frontend.utils.set_bot_commands import set_default_commands


class VacancyBot:

    def __init__(self) -> None:

        self.bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

        # storage = RedisStorage2(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
        storage = MemoryStorage()

        self.dp = Dispatcher(self.bot, storage=storage)

    # aiogram requires dispatcher to be here, even if it is not used directly
    async def on_startup(self, dispatcher: Dispatcher):

        logging.debug('On startup')

        middlewares.setup(self.dp)
        handlers.errors.setup(self.dp)
        handlers.users.setup(self.dp)

        await set_default_commands(self.dp)
        await on_startup_notify(self.dp)

    # aiogram requires dispatcher to be here, even if it is not used directly
    async def on_shutdown(self, dispatcher: Dispatcher):

        await self.dp.storage.close()
        await self.dp.storage.wait_closed()
        await self.bot.close()

    def start(self):
        executor.start_polling(self.dp, on_startup=self.on_startup, on_shutdown=self.on_shutdown)
