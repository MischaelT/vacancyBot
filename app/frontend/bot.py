from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from frontend.handlers.users import start

from frontend.data import config

from frontend import middlewares, filters, handlers
from frontend.utils.notify_admins import on_startup_notify
from frontend.utils.set_bot_commands import set_default_commands

from aiogram import executor


class VacancyBot:

    def __init__(self) -> None:
        self.bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
        storage = MemoryStorage()
        self.dp = Dispatcher(self.bot, storage=storage)
        # self.request = []
        # self.reply = []


    async def on_startup(self, dispatcher):
        from frontend import middlewares
        from frontend import filters
        from frontend import handlers
        middlewares.setup(self.dp)
        filters.setup(self.dp)
        handlers.errors.setup(self.dp)
        handlers.users.setup(self.dp)
        self.dp.register_message_handler(self.user_want_vacancy, commands= ['vacancy'])

        # Устанавливаем дефолтные команды
        await set_default_commands(dispatcher)
        # Уведомляет про запуск
        await on_startup_notify(dispatcher)

    def start(self):
        executor.start_polling(self.dp, on_startup=self.on_startup)

    # async def user_want_vacancy(self, args):
    #     self.request.append('get_vacancy')

    # async def send_message(self, text):
    #     await self.bot.send_message(285065400, self.reply)