from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from frontend.data import config
from frontend.utils.notify_admins import on_startup_notify
from frontend.utils.set_bot_commands import set_default_commands


class VacancyBot:

    def __init__(self) -> None:
        self.backend_manager = config.backend_manager
        self.bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
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
        executor.start_polling(self.dp, on_startup=self.on_startup)
