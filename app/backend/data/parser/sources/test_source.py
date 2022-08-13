import logging
import random

from backend.data.db.choices import BACKEND, DEVELOPMENT
from backend.data.parser.sources.base_source import BaseSource
from backend.data.parser.sources.consts import DOU_DATA
from backend.models.vacancy import Vacancy

from bs4 import BeautifulSoup

import requests


class TestSource(BaseSource):

    def __init__(self) -> None:

        self.settings: dict = DOU_DATA

        self.languages = self.settings['dou_languages']
        self.experiences = self.settings['dou_exp_levels']
        self.root = self.settings['root']
        self.basepoint = self.settings['basepoint']

        super().__init__()

    def make_futures(self):
        pass

    def get_content(self, page: int, language: str, experience: str) -> None:
        """
            Method connects to djinni.ua and get information.
            Then call function parse_djinni_data()

        Args:
            page (int): page for parsing
            language (str): language for params
            experience (str): eperience for params
        """

        logging.info(f'parse dou: page: {page}, language: {language}, experience: {experience}')

        proxy = 'http//:' + random.choice(self.proxies_list)
        header = random.choice(self.user_agents_list)

        headers = {'User-Agent': header}
        proxies = {'http': proxy}

        params = {}

        params['page'] = page
        params['exp'] = experience
        params['category'] = language

        url = self.root + self.basepoint

        response = requests.get(url, headers=headers, params=params, proxies=proxies)
        response.raise_for_status()

        self.parse_content(content=response.text,
                           language=language,
                           experience=experience)

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
        vacancies_data = soup.find_all('li', class_='l-vacancy')

        for vacancy_data in vacancies_data:

            title = vacancy_data.find('a', class_='vt').text.strip()
            info = vacancy_data.find('div', class_='sh-info').text.strip()
            city = vacancy_data.find('span', class_='cities').text.strip()
            link = vacancy_data.find('a', class_='vt')['href']

            vacancy = Vacancy(
                title=title,
                info=info,
                language=language,
                area=DEVELOPMENT,
                position=BACKEND,
                experience=experience,
                company_name='company_name',
                country='Ukraine',
                city=city,
                salary='salary',
                remote='remote',
                link=link,
                is_actual=True
            )

            self.parsed_data.append(vacancy)
