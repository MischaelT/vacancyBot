from backend.data.user_data_manager import User_data_manager  # noqa
from backend.data.vacancy_filter import Vacancy_filter  # noqa
from backend.data.parse_manager import ParseManager  # noqa
from backend.user import User  # noqa


class AppFlow_manager():

    def __init__(self, bot) -> None:
        self.bot = bot
        self.user_data_manager = User_data_manager()
        self.vacancy_filter = Vacancy_filter()
        self.parse_manager = ParseManager()


    def start(self):

        self.bot.start()
