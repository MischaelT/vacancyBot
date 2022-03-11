from celery import Celery
from backend.models.user import User

from backend.data.db.postgres import Db_manager
from backend.data.parser.parse_manager import ParseManager  # noqa
from backend.data.user_data_manager import User_data_manager  # noqa
from backend.data.vacancy_data_manager import Vacancies_manager  # noqa

# app = Celery('hello', broker='amqp://guest@localhost//')

class Backend_manager():

    def __init__(self) -> None:

        manager = Db_manager()
        self.user_data_manager = User_data_manager(manager)
        self.vacancies_manager = Vacancies_manager(manager)
        

    async def run_general_parsing(self):
        parse_manager = ParseManager(self.vacancies_manager)
        await parse_manager.run_general_parsing()

    async def get_vacancies(self, user: User):
        return self.vacancies_manager.get_data_by_filter(user)
