import requests
from backend.data.vacancy_data_manager import VacanciesManager
from backend.data.parser.sources.base_source import BaseSource

from bs4 import BeautifulSoup

from backend.data.parser.consts import (DATA, djinni_exp_levels,
                                        djinni_languages, dou_exp_levels,
                                        dou_languages)

import asyncio
import logging
import random

class DjinniSource(BaseSource):

    def __init__(self) -> None:

        super().__init__()


    async def get_content(self, page: int, language: dict, experience: dict):

        """
        Method connects to djinni.ua and get information.
        Then call function parse_djinni_data()

        Args:
            page (int): page for parsing
            language (dict): language for params
            experience (dict): experience for params
        """

        logging.info(f'parse djinni: page: {page}, language: {language}, experience: {experience}')

        self.headers['User-Agent'] = random.choice(self.user_agents_list)
        self.proxy['http'] += random.choice(self.proxies_list)

        settings = DATA.get('djinni')

        basepoint = settings.get('basepoint')
        endpoint = settings.get('endpoint')
        params = settings.get('params')

        params['page'] = page

        params['exp_level'] = list(experience.keys())[0]
        params['keywords'] = list(language.keys())[0]

        response = requests.get(basepoint+endpoint, headers=self.headers, params=params, proxies=self.proxy)
        response.raise_for_status()

        self.parse_content(
                            response.text,
                            basepoint=basepoint,
                            language=list(language.values())[0],
                            experience=list(experience.values())[0]
                            )

    def make_futures(self, page):

        """
            Method generates list of asyncio tasks.
            Randomly adds asyncio.sleep() task to be polite to server

        Returns:
            list: task list
        """

        tasks = []

        for language in djinni_languages:
            for exp in djinni_exp_levels:

                task = asyncio.ensure_future(self.get_content(page, language, exp))
                tasks.append(task)

        return tasks

    def parse_content(self, content: str, basepoint: str, language: str, experience: str) -> None:  # noqa
        
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
        vacancies = soup.find_all('li', class_='list-jobs__item')

        for vacancy in vacancies:

            title = vacancy.find('div', class_="list-jobs__title").text.strip()
            info = vacancy.find('div', class_='list-jobs__description').text.strip()
            link = basepoint + vacancy.find('a', class_="profile")['href']

            try:
                remote = vacancy.find('span', class_="icon icon-home_work").next_sibling.text.strip()
            except AttributeError:
                remote = ''

            try:
                cities = vacancy.find('nobr', class_="location-text").text.strip()
            except AttributeError:
                cities = remote

            data = {
                    'title': title,
                    'city': cities,
                    'info': info,
                    'link': link,
                    'language': language,
                    'experience': experience,
                }

            self.parsed_data.append(data)



