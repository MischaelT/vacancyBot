import asyncio
import random
from asyncio.events import new_event_loop, set_event_loop

from bs4 import BeautifulSoup

import requests

DATA = {
    'dou': {
            'basepoint': 'http://jobs.dou.ua',
            'endpoint': '/vacancies/',
            'params': {
                        'category': 'Python',
                        'exp': '0-1',
                    },
    },
    'djinni': {
        'basepoint': 'https://djinni.co',
        'endpoint': '/jobs/keyword-python/remote/',
        'params': {
                    'exp_level': 'no_exp',
                    'remote_type': 'full_remote',
                    'keywords': 'Python junior',
                }
    },
    'work': {
        'basepoint': 'https://www.work.ua',
        'endpoint': '/jobs-python/',
        'params': {},
    }
}


class ParseManager:

    def __init__(self, manager) -> None:

        self.db = manager
        self.headers = {'User-Agent': ''}
        self.proxy = ''

    async def run_general_parsing(self) -> None:

        loop = new_event_loop()
        set_event_loop(loop)

        page = 0
        user_agents = []

        with open('user-agents.txt', 'r') as f:
            user_agents = f.read().split('\n')

        with open('proxies.txt', 'r') as f:
            proxies = f.read().split('\n')

        while True:

            self.headers['User-Agent'] = random.choice(user_agents)
            self.proxy = 'http://'+random.choice(proxies)

            page += 1

            # TODO Implement exception handling

            result = await asyncio.gather(  # noqa
                                self.__get_content(page, site_name='dou'),
                                self.__get_content(page, site_name='djinni'),
                                self.__get_content(page, site_name='work'),
                                return_exceptions=True
                                )
            # if page == 1:
            #     break

    async def __get_content(self, page: int, site_name: str) -> None:

        settings = DATA.get(site_name)

        basepoint = settings.get('basepoint')
        endpoint = settings.get('endpoint')
        params = settings.get('params')
        params['page'] = page

        proxy = {'http': self.proxy}

        response = requests.get(basepoint+endpoint, headers=self.headers, params=params, proxies=proxy)
        response.raise_for_status()

        if site_name == 'dou':

            await asyncio.sleep(random.uniform(2, 6))
            await self.__parse_dou_data(response.text)

        if site_name == 'djinni':

            await asyncio.sleep(random.uniform(2, 6))
            await self.__parse_djinni_data(response.text, basepoint=basepoint)

        if site_name == 'work':

            await asyncio.sleep(random.uniform(2, 6))
            await self.__parse_workUa_data(response.text, basepoint=basepoint)

    async def __parse_dou_data(self, content) -> None:

        soup = BeautifulSoup(content, 'html.parser')
        vacancies = soup.find_all('li', class_='l-vacancy')

        remote = 'remote'

        for vacancy in vacancies:

            title = vacancy.find('a', class_='vt').text.strip()
            info = vacancy.find('div', class_='sh-info').text.strip()
            link = vacancy.find('a', class_='vt')['href']
            cities = vacancy.find('span', class_='cities').text.strip()

            data = {'title': title, 'city': cities, 'info': info, 'link': link, 'remote': remote}

            self.db.push_data(data)

    async def __parse_djinni_data(self, content, basepoint) -> None:

        soup = BeautifulSoup(content, 'html.parser')
        vacancies = soup.find_all('li', class_='list-jobs__item')

        for vacancy in vacancies:

            title = vacancy.find('div', class_="list-jobs__title").text.strip()
            info = vacancy.find('div', class_='list-jobs__description').text.strip()
            link = basepoint + vacancy.find('a', class_="profile")['href']
            remote = vacancy.find('span', class_="icon icon-home_work").next_sibling.text.strip()

            try:
                cities = vacancy.find('nobr', class_="location-text").text.strip()
            except AttributeError:
                cities = ''

            data = {'title': title, 'city': cities, 'info': info, 'link': link, 'remote': remote}

            self.db.push_data(data)

    async def __parse_workUa_data(self, content, basepoint) -> None:

        soup = BeautifulSoup(content, 'html.parser')
        vacancies = soup.find_all('div', class_='card card-hover card-visited wordwrap job-link')

        for vacancy in vacancies:

            title = vacancy.find('h2').text.strip()
            info = vacancy.find('p', class_='overflow text-muted add-top-sm cut-bottom').text.strip()
            link = basepoint + vacancy.find('a', class_='no-decoration')['href']
            # remote = vacancy.find('span', class_ = "icon icon-home_work").next_sibling.text.strip()
            # parsed_info_salary = self.__parse_workUa_vacancy(link)

            # info = parsed_info_salary['info']
            # salary = parsed_info_salary['salary']
            salary = ''
            data = {'title': title, 'city': '', 'info': info, 'link': link, 'salary': salary}

            self.db.push_data(data)

    async def __parse_workUa_vacancy(self, link) -> dict:

        response = requests.get(link, headers=self.headers)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        result = {}

        try:
            info = soup.find('div', id='job-description').text
        except AttributeError:
            info = ''

        result['info'] = info

        try:
            salary = soup.find('b', class_='text-black').text
        except AttributeError:
            salary = ''

        result['salary'] = salary

        return result
