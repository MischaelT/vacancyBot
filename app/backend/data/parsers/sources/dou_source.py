from aiohttp import parse_content_disposition
import requests
from backend.data.vacancy_data_manager import Vacancies_manager
from backend.data.parsers.sources.base_source import BaseSource

from bs4 import BeautifulSoup

from backend.data.parsers.consts import (DATA, djinni_exp_levels,
                                        djinni_languages, dou_exp_levels,
                                        dou_languages)

import asyncio
import logging
import random

class DouSource(BaseSource):

    def __init__(self, manager:Vacancies_manager) -> None:

        self.manager = manager
        super().__init__()


    async def get_content(self, page: int, language: str, experience: str):
        """
            Method connects to djinni.ua and get information.
            Then call function parse_djinni_data()

        Args:
            page (int): page for parsing
            language (str): language for params
            experience (str): eperience for params
        """

        logging.info(f'parse dou: page: {page}, language: {language}, experience: {experience}')

        self.headers['User-Agent'] = random.choice(self.user_agents_list)
        self.proxy['http'] += random.choice(self.proxies_list)

        settings = DATA.get('dou')

        basepoint = settings.get('basepoint')
        endpoint = settings.get('endpoint')
        params = settings.get('params')

        params['page'] = page

        params['exp'] = list(experience.keys())[0]
        params['category'] = list(language.keys())[0]


        response = requests.get(basepoint+endpoint, headers=self.headers, params=params, proxies=self.proxy)
        response.raise_for_status()
        logging.debug('Here')
        self.parse_content(content=response.text,
                           language=list(language.values())[0],
                           experience=list(experience.values())[0])



    def make_futures(self, page):

        """
            Method generates list of asyncio tasks.
            Randomly adds asyncio.sleep() task to be polite to server

        Returns:
            list: task list
        """

        tasks = []

        for language in dou_languages:
            for exp in dou_exp_levels:

                task = asyncio.ensure_future(self.get_content(page, language, exp))
                tasks.append(task)

        return tasks

    def parse_content(self, content: str, language: str, experience: str) -> None:
    
        """
            Method parses vacancies from dou.ua content

        Args:
            vacancy_manager (Vacancies_manager)
            content (str): site content
            basepoint (str): url basepoint
            language (str): language for writing to db
            experience (str): experience for writing to db
        """

        soup = BeautifulSoup(content, 'html.parser')
        vacancies = soup.find_all('li', class_='l-vacancy')

        vacancies_list = []

        for vacancy in vacancies:

            title = vacancy.find('a', class_='vt').text.strip()
            info = vacancy.find('div', class_='sh-info').text.strip()
            city = vacancy.find('span', class_='cities').text.strip()
            link = vacancy.find('a', class_='vt')['href']

            data = {
                    'title': title,
                    'city': city,
                    'info': info,
                    'link': link,
                    'language': language,
                    'experience': experience,
                    'salary': ''
                    }

            vacancies_list.append(data)

        self.manager.push_pure_data(vacancies_data=vacancies_list)



