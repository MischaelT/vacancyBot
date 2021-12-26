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
        self.is_active = True


    async def run(self):

        while self.is_active:
     
            try:
                current_request = self.bot.request[0]
            except IndexError:
                continue

            if current_request == 'get_vacancy':
                response_data = self.vacancy_filter.get_data_by_filter()
                await self.bot.send_message(response_data)

