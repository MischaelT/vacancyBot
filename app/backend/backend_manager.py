from backend.data.user_data_manager import User_data_manager  # noqa
from backend.data.vacancy_filter import Vacancy_filter  # noqa
from backend.data.parser.parse_manager import ParseManager  # noqa


class Backend_manager():

    def __init__(self) -> None:

        self.user_data_manager = User_data_manager()
        self.vacancy_filter = Vacancy_filter()
        self.parse_manager = ParseManager()

    async def run(self):
        pass
        # await self.parse_manager.run_general_parsing()

    async def get_latest_vacanvies(self):
        return self.vacancy_filter.get_data_by_filter('')
