import unicodedata
from backend.data.db.postgres import Postgres_db
from backend.models.user import User
from backend.models.vacancy import Vacancy

import re

import logging


class Vacancies_manager():

    """
    Class provides methods for interaction with vacancies data
    """

    def __init__(self, manager: Postgres_db) -> None:
        self.db = manager

    def get_data_by_filter(self, user: User) -> list:

        """
        Public method that returns vacancies for given user

        Args:
            user (User): user model

        Returns:
            list: list of vacancies
        """

        return self.__get_data(user)

    def push_pure_data(self, vacancies_data: list) -> None:

        """
        Method pushes pure data after parsing to db

        Args:
            vacancies_data (list): list os dicts with vacancy data
        """

        date = '2022-03-10'
        params = []

        for vacancy in vacancies_data:

            self.__preprocess_vacancies_data(vacancies_data=vacancy)

            params = (
                date,
                vacancy['experience'],
                vacancy['language'],
                vacancy['city'],
                vacancy['title'],
                vacancy['info'],
                vacancy['link'],
                '1000',
            )

            query = '''INSERT INTO vacancies (date, exp, lang, city, title, info, link, salary)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                    '''

            self.db.push_data(query, params)

    def __get_data(self, user: User) -> list:

        """
        Method gets 10 latest vacancies from db with given filter

        Args:
            user (User): user model

        Returns:
            list: list of vacancy models
        """

        vacancies = []

        params = (user.experience, user.language)

        query = '''SELECT date,title,city,info,link FROM vacancies
                    WHERE exp=%s AND lang=%s;
                    '''

        responce = self.db.get_data(query, params=params)

        # TODO Implement getting latest vacancies

        i = 0

        for element in responce:
            i += 1

            vacancy = self.__create_vacancy(element)
            vacancies.append(vacancy)

            if i > 10:
                break

        return vacancies

    def __create_vacancy(self, data: dict) -> Vacancy:
        """
        Method creates new vacancy model from given data

        Args:
            data (dict): vacancy data

        Returns:
            Vacancy: vacancy model
        """

        vacancy = Vacancy(
            date=data[0],
            title=data[1],
            city=data[2],
            info=data[3],
            link=data[4],
        )

        return vacancy


    def __preprocess_vacancies_data(self, vacancies_data):
        
        vacancies_data['info'] = re.sub('/[\r\n]+/g', '\n', vacancies_data['info'])
        vacancies_data['info'] = re.sub(" +", " ", vacancies_data['info'])

        vacancies_data['title'] = re.sub('/[\r\n]+/g', '\n', vacancies_data['title'])
        vacancies_data['title'] =re.sub(" +", " ", vacancies_data['title'])

        title_text = vacancies_data['title'].lower().split()

        vacancies_data['info'] = unicodedata.normalize("NFKD", vacancies_data['info'])
        vacancies_data['title'] = unicodedata.normalize("NFKD", vacancies_data['title'])

        if 'devops' in title_text:
            vacancies_data['language'] = 'DevOps'

        for word in ['kotlin', 'android']:
            if word in title_text:
                vacancies_data['language'] = 'Android'

        for word in ['data', 'ml', 'deep', 'analyst', 'learning']:
            if word in title_text:
                vacancies_data['language'] = 'Data'

        for word in ['qa', 'test', 'automation']:
            if word in title_text:
                vacancies_data['language'] = 'QA'

        for word in ['blockchain', 'solidity']:
            if word in title_text:
                vacancies_data['language'] = 'blockchain'

        
