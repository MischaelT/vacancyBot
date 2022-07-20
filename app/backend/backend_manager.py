from backend.data.db.postgres import Postgres_db
from backend.data.parsers.parse_manager import ParseManager
from backend.data.user_data_manager import User_data_manager
from backend.data.vacancy_data_manager import Vacancies_manager


class Backend_manager():

    """
    Class for interacting with backend
    """

    def __init__(self) -> None:

        manager = Postgres_db()
        self.user_data_manager = User_data_manager(manager)
        self.vacancies_manager = Vacancies_manager(manager)

    async def run_general_parsing(self):

        """
        Method runs parsing for all sources, for all languages and experiences from parser/consts.py
        """

        parse_manager = ParseManager(self.vacancies_manager)

        await parse_manager.run_general_parsing()
