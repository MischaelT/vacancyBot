# from backend.data.storage.json_manager import Json_manager as manager
# from backend.data.storage.csv_manager import Csv_manager as manager
from asyncio.events import new_event_loop, set_event_loop
import typing
from backend.data.storage.db_manager import Db_manager as manager

import asyncio

from bs4 import BeautifulSoup

import requests


class ParseManager:

    def __init__(self) -> None:

        self.db = manager()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    async def run_general_parsing(self) -> None:

        loop = new_event_loop()

        set_event_loop(loop)

        page = 0

        while True:

            page += 1

            # TODO Implement exception handling
            

            result = await asyncio.gather(
                                self.__get_dou_content(page),
                                self.__get_djinni_content(page),
                                self.__get_workUa_content(page),
                                return_exceptions=True
                                )
            for website in result:
                print(type(website))

            
            print(result)

    async def __get_dou_content(self, page) -> None:

        basepoint = 'http://jobs.dou.ua'
        endpoint = '/vacancies/'

        params = {
            'category': 'Python',
            'exp': '0-1',
            'page': page,
        }

        response = requests.get(basepoint+endpoint, headers=self.headers, params=params)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        await self.__parse_dou_data(soup)

    async def __get_djinni_content(self, page) -> None:

        basepoint = 'https://djinni.co'
        endpoint = '/jobs/keyword-python/remote/'

        params = {
            'page': page,
            'exp_level': 'no_exp',
            'remote_type': 'full_remote',
            'keywords': 'Python junior'
        }

        response = requests.get(basepoint+endpoint, headers=self.headers, params=params)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        await self.__parse_djinni_data(soup, basepoint)

    async def __get_workUa_content(self, page) -> None:

        basepoint = 'https://www.work.ua'
        endpoint = '/jobs-python/'

        params = {
            'page': page
        }

        response = requests.get(basepoint+endpoint, params=params, headers=self.headers)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        await self.__parse_workUa_data(soup, basepoint)

    async def __parse_dou_data(self, soup) -> None:

        vacancies = soup.find_all('li', class_='l-vacancy')

        remote = 'remote'

        for vacancy in vacancies:

            title = vacancy.find('a', class_='vt').text.strip()
            info = vacancy.find('div', class_='sh-info').text.strip()
            link = vacancy.find('a', class_='vt')['href']
            cities = vacancy.find('span', class_='cities').text.strip()

            data = {'title': title, 'city': cities, 'info': info, 'link': link, 'remote': remote}

            self.db.push_data(data)

    async def __parse_djinni_data(self, soup, basepoint) -> None:

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

    async def __parse_workUa_data(self, soup, basepoint) -> None:

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
