import asyncio
import logging

from backend.data.db.postgres import PostgresDB
from backend.data.parser.parse_manager import ParseManager
from backend.data.user_data_manager import UserDataManager
from backend.data.vacancy_data_manager import VacanciesManager


class BackendManager():

    """
    Class for interacting with backend
    """

    def __init__(self) -> None:

        logging.info('BackendManager created')

        self.db = PostgresDB()

        self.user_data_manager = UserDataManager(self.db)
        self.vacancies_manager = VacanciesManager(self.db)

    #  message need because aiogram requires this variable to be in method signature
    async def run_async_parsing(self, message) -> None:

        """
        Method runs parsing for all sources, for all languages and experiences from parser/consts.py
        """

        logging.info('Begin general parsing')

        parse_manager = ParseManager()

        self.db.clear_vacancy_table()

        vacancies = await parse_manager.run_parsing()

        self.vacancies_manager.preprocess_vacancy_data(vacancies=vacancies)

        self.vacancies_manager.push_to_db(vacancies=vacancies)

        logging.info('End general parsing')

    def run_parsing(self) -> None:

        """
        Method runs parsing for all sources, for all languages and experiences from parser/consts.py
        """

        logging.info('Begin general parsing')

        parse_manager = ParseManager()

        self.db.clear_vacancy_table()

        vacancies = asyncio.run(parse_manager.run_parsing())

        self.vacancies_manager.preprocess_vacancy_data(vacancies=vacancies)

        self.vacancies_manager.push_to_db(vacancies=vacancies)

        logging.info('End general parsing')
