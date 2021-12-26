# from backend.data.storage.json_manager import Json_manager as manager
# from backend.data.storage.csv_manager import Csv_manager as manager
from backend.data.storage.db_manager import Db_manager as manager

from bs4 import BeautifulSoup

import requests


class ParseManager:

    def __init__(self) -> None:

        self.db = manager()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def parse_douUA(self):

        url = 'http://jobs.dou.ua/vacancies/'

        page = 0

        params = {
            'category': 'Python',
            'exp': '0-1',
            'page': page,
        }

        while True:

            page += 1

            params['page'] = page

            response = requests.get(url, headers=self.headers, params=params)

            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            vacancies = soup.find_all('li', class_='l-vacancy')

            if len(vacancies) == 0:
                break

            remote = 'remote'

            for vacancy in vacancies:

                title = vacancy.find('a', class_='vt').text.strip()
                info = vacancy.find('div', class_='sh-info').text.strip()
                link = vacancy.find('a', class_='vt')['href']
                cities = vacancy.find('span', class_='cities').text.strip()

                data = {'title': title, 'city': cities, 'info': info, 'link': link, 'remote': remote}

                self.db.push_data(data)

    def parse_djinniCo(self):

        basepoint = 'https://djinni.co'
        url = 'https://djinni.co/jobs/keyword-python/remote/'

        page = 0

        params = {
            'page': page,
            'exp_level': 'no_exp',
            'remote_type': 'full_remote',
            'keywords': 'Python junior'
        }

        while True:

            page += 1

            params['page'] = page

            response = requests.get(url, headers=self.headers, params=params)

            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            vacancies = soup.find_all('li', class_='list-jobs__item')

            if len(vacancies) == 0:
                break

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

    def parse_workUa(self):

        base_url = 'https://www.work.ua'
        endpoint = '/jobs-python/'
        page = 0

        params = {
            'page': page
        }

        while True:

            page += 1

            params['page'] = page

            response = requests.get(base_url+endpoint, params=params, headers=self.headers)

            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            vacancies = soup.find_all('div', class_='card card-hover card-visited wordwrap job-link')

            if len(vacancies) == 0:
                break

            for vacancy in vacancies:

                title = vacancy.find('h2').text.strip()
                info = vacancy.find('p', class_='overflow text-muted add-top-sm cut-bottom').text.strip()
                link = base_url + vacancy.find('a', class_='no-decoration')['href']
                # remote = vacancy.find('span', class_ = "icon icon-home_work").next_sibling.text.strip()
                parsed_info_salary = self.__parse_workUa_vacancy(link)

                # info = parsed_info_salary['info']
                salary = parsed_info_salary['salary']

                data = {'title': title, 'city': '', 'info': info, 'link': link, 'salary': salary}
                self.db.push_data(data)

    def __parse_workUa_vacancy(self, link):

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
