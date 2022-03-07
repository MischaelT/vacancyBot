
from backend.models.vacancy import Vacancy


class Vacancy_filter():

    def __init__(self, manager) -> None:
        self.db = manager

    def get_data_by_filter(self, user) -> list:

        vacancies = self.__get_data(user)

        for i in range(10):
            pure_vacancy = self.db.get_data(id_=i)
            vacancy = self.__create_vacancy(pure_vacancy[0])
            vacancies.append(vacancy)

        return vacancies

    def __get_data(self, user):

        # TODO Implement creating query from user data

        query = ''
        return self.manager.get_data(query)

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
