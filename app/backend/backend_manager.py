import asyncio
import logging

from backend.data.db.postgres import Postgres_db
from backend.data.parser.parse_manager import ParseManager
from backend.data.user_data_manager import User_data_manager
from backend.data.vacancy_data_manager import VacanciesManager


class Backend_manager():

    """
    Class for interacting with backend
    """

    def __init__(self) -> None:

        logging.info('BackendManager created')

        self.db = Postgres_db()

        self.user_data_manager = User_data_manager(self.db)
        self.vacancies_manager = VacanciesManager(self.db)

    async def run_general_parsing(self):

        """
        Method runs parsing for all sources, for all languages and experiences from parser/consts.py
        """

        logging.info('Begin general parsing')

        parse_manager = ParseManager()

        self.db.clear_vacancy_table()

        parsed_data = await parse_manager.run_general_parsing()

        self.vacancies_manager.preprocess_vacancy_data(parsed_data=parsed_data)

        vacancies = self.vacancies_manager.data_to_vacancies(parsed_data)

        self.vacancies_manager.push_to_db(vacancies=vacancies)

        logging.info('End general parsing')