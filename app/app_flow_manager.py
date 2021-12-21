from backend.data.user_data_manager import User_data_manager  # noqa
from backend.data.vacancy_filter import Vacancy_filter  # noqa
from backend.data.parse_manager import ParseManager  # noqa
from backend.user import User  # noqa

from aiogram import executor  # noqa

# from frontend import middlewares, filters, handlers
# from frontend.utils.notify_admins import on_startup_notify
# from frontend.utils.set_bot_commands import set_default_commands


class appFlow_manager():

    def __init__(self) -> None:
        # self.bot = bot
        self.user_data_manager = User_data_manager()
        self.vacancy_filter = Vacancy_filter()
        self.parse_manager = ParseManager()

    # async def on_startup(self, dispatcher):
    #     # Устанавливаем дефолтные команды
    #     await set_default_commands(dispatcher)

    #     # Уведомляет про запуск
    #     await on_startup_notify(dispatcher)

    def start(self):
        # dp = self.bot.dp
        # executor.start_polling(dp, on_startup=self.on_startup)
        self.parse_manager.parse_workUa()
