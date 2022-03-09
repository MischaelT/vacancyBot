from backend.models.vacancy import Vacancy


class Vacancies_manager():

    def __init__(self, manager) -> None:
        self.db = manager

    def get_data_by_filter(self, user) -> list:
        pass

    def make_vacancy(self, data):
        self.__create_vacancy(data)

    def __get_data(self, user):
        pass

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


    def push_pure_data(self, vacancies_data: list):
        for vacancy in vacancies_data:
            query = f'''INSERT INTO vacancy (id, is_registered, exp, lang, city, salary)
                VALUES ('{vacancy['']}', '{user.is_registered}', '{user.experience}', '{user.language}', '{user.city}', '{user.salary}')
            '''
        self.db.push_data(query)