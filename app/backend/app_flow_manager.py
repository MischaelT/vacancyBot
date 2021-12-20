from data.user_data_manager import User_data_manager
from data.vacancy_filter import Vacancy_filter
from data.parse_manager import ParseManager
from user import User


class appFlow_manager():

    def __init__(self, bot) -> None:
        self.bot = bot
        self.user_data_manager = User_data_manager()
        self.vacancy_filter = Vacancy_filter()
        self.parse_manager = ParseManager()



