from backend.data.db.postgres import Db_manager
from backend.data.parser.parse_manager import ParseManager  # noqa
from backend.data.user_data_manager import User_data_manager  # noqa
from backend.data.vacancy_data_manager import Vacancy_filter  # noqa


class Backend_manager():

    def __init__(self) -> None:

        manager = Db_manager()
        self.user_data_manager = User_data_manager(manager)
        self.vacancy_filter = Vacancy_filter(manager)
        self.parse_manager = ParseManager(manager)

    async def run(self):
        pass
        # await self.parse_manager.run_general_parsing()

    async def get_latest_vacanvies(self):
        return self.vacancy_filter.get_data_by_filter('')
