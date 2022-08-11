import logging

from aiogram import Bot, Dispatcher, executor, types
# from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from backend.tasks import initialise_sceduler

from backend.backend_manager import BackendManager

from frontend.utils.notify_admins import on_startup_notify
from frontend.utils.set_bot_commands import set_default_commands
# from frontend.data.config import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT

from settings import config


class VacancyBot:

    def __init__(self, backend_manager: BackendManager) -> None:

        self.backend_manager = backend_manager
        self.bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
        # storage = RedisStorage2(host=REDIS_HOST, port=REDIS_PORT, password=None)

        storage = MemoryStorage()
        self.dp = Dispatcher(self.bot, storage=storage)

    async def on_startup(self, dispatcher: Dispatcher):

        from frontend import handlers, middlewares

        logging.debug('On startup')

        middlewares.setup(self.dp)
        handlers.errors.setup(self.dp)
        handlers.users.setup(self.dp)

        # initialise_sceduler()

        await set_default_commands(self.dp)
        await on_startup_notify(self.dp)

    def start(self):

        executor.start_polling(self.dp, on_startup=self.on_startup, on_shutdown=self.on_shutdown)

    async def on_shutdown(self, dispatcher: Dispatcher):

        await self.bot.close()
