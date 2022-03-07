from aiogram import Bot, Dispatcher, executor, types
# from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from frontend.utils.notify_admins import on_startup_notify
from frontend.utils.set_bot_commands import set_default_commands

from settings import config

# from frontend.data.config import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT


class VacancyBot:

    def __init__(self) -> None:
        self.backend_manager = config.backend_manager
        self.bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
        # storage = RedisStorage2(host=REDIS_HOST, port=REDIS_PORT, password=None)

        storage = MemoryStorage()
        self.dp = Dispatcher(self.bot, storage=storage)

    async def on_startup(self, dispatcher):

        from frontend import filters, handlers, middlewares

        middlewares.setup(self.dp)
        filters.setup(self.dp)
        handlers.errors.setup(self.dp)
        handlers.users.setup(self.dp)

        # Устанавливаем дефолтные команды
        await set_default_commands(dispatcher)
        # Уведомляет про запуск
        await on_startup_notify(dispatcher)

        self.dp.register_message_handler

    def start(self):
        executor.start_polling(self.dp, on_startup=self.on_startup, on_shutdown=self.on_shutdown)

    async def on_shutdown(self, dp):
        await self.bot.close()
