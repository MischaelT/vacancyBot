from backend.models.user import User
from backend.data.db.postgres import Db_manager
from backend.models.vacancy import Vacancy

class Vacancies_manager():

    def __init__(self, manager: Db_manager) -> None:
        self.db = manager

    def get_data_by_filter(self, user: User) -> list:
        return self.__get_data(user)

    def make_vacancy(self, data) -> Vacancy:
        return self.__create_vacancy(data)

    async def push_pure_data(self, vacancies_data: list) -> None:

        # TODO Разобраться datetime

        date = '2022-03-10'

        for vacancy in vacancies_data:

            query = f'''INSERT INTO vacancies (date, exp, lang, city, title, info, link, salary)
                        VALUES (
                            '{date}', '{vacancy['experience']}', 
                            '{vacancy['language']}', '{vacancy['city']}', 
                            '{vacancy['title']}', '{vacancy['info']}',
                            '{vacancy['link']}', '1000'
                        );
                    '''

            self.db.push_data(query)

    def __get_data(self, user: User) -> list:

        vacancies = []

        query = f'''SELECT date,title,city,info,link FROM vacancies
                    WHERE exp='{user.experience}' AND lang='{user.language}';
                    '''


        responce = self.db.get_data(query)

        for element in responce:

            vacancy = self.__create_vacancy(element)
            vacancies.append(vacancy)

        return vacancies

    def __create_vacancy(self, data) -> Vacancy:

        vacancy = Vacancy(
            date=data[0],
            title=data[1],
            city=data[2],
            info=data[3],
            link=data[4],
        )

        print(vacancy.to_print()) 

        return vacancy
