# from backend.data.storage.json_manager import Json_manager as manager
# from backend.data.storage.csv_manager import Csv_manager as manager
from backend.data.storage.db_manager import Db_manager as manager
from backend.data.vacancy import Vacancy


class Vacancy_filter():

    def __init__(self) -> None:
        self.db = manager()

    def get_data_by_filter(self, filter_) -> list:

        vacancies = []

        for i in range(10):
            pure_vacancy = self.db.get_data(id_=i)
            vacancy = self.__create_vacancy(pure_vacancy[0])
            vacancies.append(vacancy)

        return vacancies

    def __create_vacancy(self, data) -> Vacancy:

        data = list(data)

        vacancy = Vacancy(
            data='',
            title=data[1],
            city='',
            info=data[3],
            link=data[4],
        )
        return vacancy
