from typing import List, Union
import unicodedata

from backend.data.db.postgres import Postgres_db
from backend.models.user import User
from backend.models.vacancy import Vacancy

import re

import logging


class VacanciesManager():

    """
    Class provides methods for interaction with vacancies data
    """

    def __init__(self, manager: Postgres_db) -> None:
        self.db = manager

    def get_user_data(self, user: User) -> List[Vacancy]:

        """
        Public method that returns vacancies for given user

        Args:
            user (User): user model

        Returns:
            list: list of vacancies
        """

        logging.info(f'Manage user with id: {user.user_id}')

        return self.__get_data(user)


    def data_to_vacancies(self, vacancies_data: List[dict]) -> List[Vacancy]:

        """
        Method pushes pure data after parsing to db

        Args:
            vacancies_data (list): list os dicts with vacancy data
        """
        vacancies: List[Vacancy] = []

        for vacancy_data in vacancies_data:

            vacancy = self.__create_vacancy(data = vacancy_data)

            vacancies.append(vacancy)
   
        return vacancies

    def preprocess_vacancy_data(self, parsed_data:List[dict]):
        for vacancy_data in parsed_data:
            vacancy_data['info'] = re.sub('/[\r\n]+/g', '\n', vacancy_data['info'])
            vacancy_data['info'] = re.sub(" +", " ", vacancy_data['info'])

            vacancy_data['title'] = re.sub('/[\r\n]+/g', '\n', vacancy_data['title'])
            vacancy_data['title'] =re.sub(" +", " ", vacancy_data['title'])

            title_text = vacancy_data['title'].lower().split()

            vacancy_data['info'] = unicodedata.normalize("NFKD", vacancy_data['info'])
            vacancy_data['title'] = unicodedata.normalize("NFKD", vacancy_data['title'])

            if 'devops' in title_text:
                vacancy_data['language'] = 'DevOps'

            for word in ['kotlin', 'android']:
                if word in title_text:
                    vacancy_data['language'] = 'Android'

            for word in ['data', 'ml', 'deep', 'analyst', 'learning']:
                if word in title_text:
                    vacancy_data['language'] = 'Data'

            for word in ['qa', 'test', 'automation']:
                if word in title_text:
                    vacancy_data['language'] = 'QA'

            for word in ['blockchain', 'solidity']:
                if word in title_text:
                    vacancy_data['language'] = 'blockchain'

            vacancy_data['id'] = '0'
            vacancy_data['area'] = 'developer'
            vacancy_data['company_name'] = 'COMPANY_NAME'
            vacancy_data['remote'] = 'remote'
            vacancy_data['salary'] = 1000
            vacancy_data['country'] = 'ukraine'
            vacancy_data['is_actual'] = True


    def refresh_db(self, new_data: List[Vacancy]):

        query = '''SELECT *
                   FROM vacancies
                   WHERE IS_ACTUAL=TRUE
                    '''
        params = ()

        old_data = self.db.get_data(query=query,params=params)
        logging.debug(old_data)
        old_vacancies = self.data_to_vacancies(old_data)


    def push_to_db(self, vacancies: List[Vacancy]):

        for vacancy in vacancies:
            params = (
                vacancy.title,
                vacancy.info,
                vacancy.language,
                vacancy.area,
                vacancy.experience,
                vacancy.company_name,
                vacancy.country,
                vacancy.city,
                vacancy.remote,
                vacancy.salary,
                vacancy.link,
                vacancy.is_actual,
            )

            self.db.push_vacancy_data(params=params)

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

        vacancies_data = self.db.get_vacancies_data(params=params)
        logging.debug(vacancies_data)

        for vacancy_data in vacancies_data:

            vacancy = self.__create_vacancy(vacancy_data)
            vacancies.append(vacancy)
        
        return vacancies

    def __create_vacancy(self, data: Union[tuple,dict]) -> Vacancy:
        """
        Method creates new vacancy model from given data

        Args:
            data (dict): vacancy data

        Returns:
            Vacancy: vacancy model
        """

        if isinstance(data, tuple):

            vacancy = Vacancy(
                id=data[0],
                title=data[1],
                info=data[2],
                language=data[3],                
                area=data[4],
                experience=data[5],
                company_name=data[6],
                country=data[7],
                city=data[8],
                remote=data[9],
                salary=data[10],
                link=data[11],
                is_actual= data[11],
            )

        elif isinstance(data, dict):

            vacancy = Vacancy(
                id_ = data['id'],
                title = data['title'],
                info = data['info'],
                language = data['language'] ,
                area = data['area'],
                experience = data['experience'],
                company_name = data['company_name'],
                country = data['country'],
                city = data['city'],
                salary = data['salary'],
                remote = data['remote'],
                link = data['link'],
                is_actual= data['is_actual'],
            )

        return vacancy

