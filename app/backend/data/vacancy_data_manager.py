import logging
import re
import unicodedata
from typing import List, Union

from backend.data.db.choices import (ANALYST, ANDROID, AUTO, BLOCKCHAIN, DATA,
                                     DEVOPS, ENGINEER, FRONTEND, MANUAL,
                                     SCIENTIST, TEST)
from backend.data.db.postgres import Postgres_db
from backend.models.user import User
from backend.models.vacancy import Vacancy


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

    # def data_to_vacancies(self, vacancies_data: List[dict]) -> List[Vacancy]:

    #     """
    #     Method pushes pure data after parsing to db

    #     Args:
    #         vacancies_data (list): list os dicts with vacancy data
    #     """
    #     vacancies: List[Vacancy] = []

    #     for vacancy_data in vacancies_data:

    #         vacancy = self.__create_vacancy(data=vacancy_data)

    #         vacancies.append(vacancy)

    #     return vacancies

    def preprocess_vacancy_data(self, vacancies: List[Vacancy]) -> None:

        for vacancy in vacancies:

            vacancy.info = re.sub('/[\r\n]+/g', '\n', vacancy.info)
            vacancy.info = re.sub(" +", " ", vacancy.info)

            vacancy.title = re.sub('/[\r\n]+/g', '\n', vacancy.title)
            vacancy.title = re.sub(" +", " ", vacancy.title)

            title_text = vacancy.title.lower().split()

            vacancy.info = unicodedata.normalize("NFKD", vacancy.info)
            vacancy.title = unicodedata.normalize("NFKD", vacancy.title)

            if 'devops' in title_text:
                vacancy.area = DEVOPS
                vacancy.position = DEVOPS

            for word in ['kotlin', 'android']:
                if word in title_text:
                    vacancy.language = ANDROID
                    vacancy.position = ANDROID

            for word in ['front', 'frontend', 'front-end']:
                if word in title_text:
                    vacancy.area = FRONTEND

            for word in ['data', 'ml', 'deep', 'analyst', 'learning', 'engineer']:
                if word in title_text:
                    vacancy.area = DATA
                    if word == 'analyst':
                        vacancy.position = ANALYST
                    elif word == 'engineer':
                        vacancy.position = ENGINEER
                    else:
                        vacancy.position = SCIENTIST

            for word in ['qa', 'test', 'automation', 'manual']:
                if word in title_text:
                    vacancy.area = TEST
                    if word == 'automation':
                        vacancy.position = AUTO
                    if word == 'manual':
                        vacancy.position = MANUAL

            for word in ['blockchain', 'solidity']:
                if word in title_text:
                    vacancy.area = BLOCKCHAIN

            vacancy.company_name = 'COMPANY_NAME'
            vacancy.salary = 1000
            vacancy.country = 'ukraine'
            vacancy.is_actual = True

    def push_to_db(self, vacancies: List[Vacancy]) -> None:

        for vacancy in vacancies:
            params = (
                vacancy.title,
                vacancy.info,
                vacancy.language,
                vacancy.area,
                vacancy.position,
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

        params = (user.experience, user.language, user.area, user.position)

        vacancies_data = self.db.get_vacancies_data(params=params)

        for vacancy_data in vacancies_data:

            vacancy = self.__create_vacancy(vacancy_data)
            vacancies.append(vacancy)

        return vacancies

    def __create_vacancy(self, data: Union[tuple, dict]) -> Vacancy:

        """
        Method creates new vacancy model from given data

        Args:
            data (dict): vacancy data

        Returns:
            Vacancy: vacancy model
        """

        vacancy = Vacancy(
            id_=data[0],
            title=data[1],
            info=data[2],
            language=data[3],
            area=data[4],
            position=data[5],
            experience=data[6],
            company_name=data[7],
            country=data[8],
            city=data[9],
            remote=data[10],
            salary=data[11],
            link=data[12],
            is_actual=data[13],
        )

        return vacancy
