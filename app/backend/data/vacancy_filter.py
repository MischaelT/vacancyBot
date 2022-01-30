# from backend.data.storage.json_manager import Json_manager as manager
# from backend.data.storage.csv_manager import Csv_manager as manager
from backend.data.vacancy import Vacancy
from backend.data.storage.db_manager import Db_manager as manager


class Vacancy_filter():
    
    def __init__(self) -> None:
        self.db = manager()

    def get_data_by_filter(self, filter) -> list:

        vacancies_data = manager.get_data()
        vacancies = []

        for _ in vacancies:
            vacancies.append(self.__create_vacancies(vacancies_data, filter))

        return vacancies

    def __create_vacancies(self, filter) -> Vacancy:
        pass