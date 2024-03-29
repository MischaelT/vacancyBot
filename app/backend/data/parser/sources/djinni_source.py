import asyncio
import logging
import random

from backend.data.db.choices import BACKEND, DEVELOPMENT, MANAGEMENT
from backend.data.parser.sources.base_source import BaseSource
from backend.data.parser.sources.consts import DJINNI_DATA
from backend.models.vacancy import Vacancy

from bs4 import BeautifulSoup

import requests


class DjinniSource(BaseSource):

    def __init__(self) -> None:

        self.settings: dict = DJINNI_DATA

        self.nonDev_positions = self.settings['non_dev_positions']
        self.languages = self.settings['djinni_languages']
        self.experiences = self.settings['djinni_exp_levels']
        self.root = self.settings['root']
        self.basepoint = self.settings['basepoint']

        super().__init__()

    def make_futures(self, page: int) -> list:

        """
            Method generates list of asyncio tasks.
            Randomly adds asyncio.sleep() task to be polite to server

        Returns:
            list: task list
        """

        tasks = []

        for experience in self.experiences:

            for position in self.nonDev_positions:
                task = asyncio.ensure_future(self._get_nonDev_vacancies(page=page, position=position, experience=experience))  # noqa
                tasks.append(task)

            for language in self.languages:
                task = asyncio.ensure_future(self._get_dev_vacancies(page=page, language=language, experience=experience))  # noqa
                tasks.append(task)

        return tasks

    async def _get_dev_vacancies(self, page: int, language: dict, experience: dict) -> None:

        """
        Method connects to djinni.ua and get information.
        Then call function parse_djinni_data()

        Args:
            page (int): page for parsing
            language (dict): language for params
            experience (dict): experience for params
        """

        logging.info(f'parse djinni: page: {page}, language: {language}, experience: {experience}')

        params = {}

        params['page'] = page
        params['exp_level'] = experience
        params['keywords'] = language

        proxy = 'http//:' + random.choice(self.proxies_list)
        header = random.choice(self.user_agents_list)

        headers = {'User-Agent': header}
        proxies = {'http': proxy}

        url = self.root + self.basepoint

        response = requests.get(url, headers=headers, params=params, proxies=proxies)
        response.raise_for_status()

        self._parse_dev_content(response.text,
                                language=self.languages[language],
                                experience=self.experiences[experience])

    def _parse_dev_content(self, content: str, language: str, experience: str) -> None:  # noqa

        """
            Method parses vacancies from djinni.ua content

        Args:
            vacancy_manager (Vacancies_manager)
            content (str): site content
            basepoint (str): url basepoint
            language (str): language for writing to db
            experience (str): experience for writing to db
        """

        soup = BeautifulSoup(content, 'html.parser')
        vacancies_data = soup.find_all('li', class_='list-jobs__item')

        for vacancy_data in vacancies_data:

            title = vacancy_data.find('div', class_="list-jobs__title").text.strip()
            info = vacancy_data.find('div', class_='list-jobs__description').text.strip()
            link = self.root + vacancy_data.find('a', class_="profile")['href']

            try:
                remote = vacancy_data.find('span', class_="icon icon-home_work").next_sibling.text.strip()
            except AttributeError:
                remote = ''

            try:
                location = vacancy_data.find('nobr', class_="location-text").text.strip()
            except AttributeError:
                location = remote

            vacancy = Vacancy(
                title=title,
                info=info,
                language=language,
                area=DEVELOPMENT,
                position=BACKEND,
                experience=experience,
                company_name='company_name',
                country='Ukraine',
                city=location,
                salary='salary',
                remote=remote,
                link=link,
                is_actual=True
            )

            self.parsed_data.append(vacancy)

    async def _get_nonDev_vacancies(self, page: int, position: str, experience: dict) -> None:

        logging.info(f'parse {position}: page: {page}, experience: {experience}')

        proxy = 'http//:' + random.choice(self.proxies_list)
        header = random.choice(self.user_agents_list)

        headers = {'User-Agent': header}
        proxies = {'http': proxy}

        endpoint = self.settings.get('non_dev_endpoint')

        params = {}
        params['page'] = page
        params['exp_level'] = experience

        url = self.root + self.basepoint + endpoint + position

        response = requests.get(url, headers=headers, params=params, proxies=proxies)
        response.raise_for_status()

        self._parse_nonDev_content(response.text,
                                   experience=self.experiences[experience],
                                   position=self.nonDev_positions[position])


    def _parse_nonDev_content(self, content: str, experience: str, position: str) -> None:  # noqa

        """
            Method parses vacancies from djinni.ua content

        Args:
            content (str): site content
            basepoint (str): url basepoint
            language (str): language for writing to db
            experience (str): experience for writing to db
        """

        soup = BeautifulSoup(content, 'html.parser')
        vacancies_data = soup.find_all('li', class_='list-jobs__item')

        for vacancy_data in vacancies_data:

            title = vacancy_data.find('div', class_="list-jobs__title").text.strip()
            info = vacancy_data.find('div', class_='list-jobs__description').text.strip()
            link = self.root + vacancy_data.find('a', class_="profile")['href']

            try:
                remote = vacancy_data.find('span', class_="icon icon-home_work").next_sibling.text.strip()
            except AttributeError:
                remote = ''

            try:
                location = vacancy_data.find('nobr', class_="location-text").text.strip()
            except AttributeError:
                location = remote

            vacancy = Vacancy(
                title=title,
                info=info,
                language='language',
                area=MANAGEMENT,
                position=position,
                experience=experience,
                company_name='company_name',
                country='Ukraine',
                city=location,
                salary='salary',
                remote=remote,
                link=link,
                is_actual=True
            )

            self.parsed_data.append(vacancy)
