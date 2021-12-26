# from backend.data.storage.json_manager import Json_manager as manager
# from backend.data.storage.csv_manager import Csv_manager as manager
from backend.data.storage.db_manager import Db_manager as manager


class Vacancy_filter():
    def __init__(self) -> None:
        self.db = manager()

    def get_data_by_filter(self) -> list:
        vacancies_data = manager.get_data()
        # self.__create_vacancies(vacancies_data)
        return vacancies_data

    def __create_vacancies(self) -> list:
        pass