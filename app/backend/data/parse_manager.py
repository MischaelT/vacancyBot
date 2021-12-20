from app.backend.data.storage.db_manager import Db_manager

import requests
from bs4 import BeautifulSoup
from string import printable
import csv

class ParseManager:

    def __init__(self) -> None:

        self.db = Db_manager()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def parse_douUA(self)->list:

        params = {
        'category': 'Python',
        'exp': '0-1'
        }
        
        url = 'http://jobs.dou.ua/vacancies/'

        response = requests.get(url, headers=self.headers, params=params)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        vacancies_list = soup.find_all('li', class_ = 'l-vacancy')

        all_vacancies_data = []
        remote='remote'

        for vacancy in vacancies_list:

            title = vacancy.find('a', class_='vt').text.strip()
            info = vacancy.find('div', class_ = 'sh-info').text.strip()
            link = vacancy.find('a', class_='vt')['href']
            cities = vacancy.find('span', class_ = 'cities').text.strip()

            # TODO
            new_info = ''.join(char for char in info if char in printable)

            data = {'title': title, 'city':cities, 'info': new_info, 'link': link, 'remote':remote}

            all_vacancies_data.append(data)

        return all_vacancies_data

    def parse_djinniCo(self)->list:

        params = {
            'exp_level': 'no_exp',
            'remote_type' : 'full_remote',
            'keywords': 'Python junior'
            }

        basepoint = 'https://djinni.co'
        url = 'https://djinni.co/jobs/keyword-python/remote/'

        response = requests.get(url, headers=self.headers, params=params)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        vacansies_list = soup.find_all('li', class_ = 'list-jobs__item')

        all_vacancies_data = []
        

        for vacancy in vacansies_list:

            title = vacancy.find('div', class_ = "list-jobs__title").text.strip()
            info = vacancy.find('div', class_ = 'list-jobs__description').text.strip()
            link = basepoint + vacancy.find('a', class_ = "profile")['href']
            remote = vacancy.find('span', class_ = "icon icon-home_work").next_sibling.text.strip()

            try:
                cities = vacancy.find('nobr', class_ = "location-text").text.strip()
            except AttributeError:
                cities = ''

            data = {'title': title, 'city':cities, 'info': info, 'link': link, 'remote': remote}

            all_vacancies_data.append(data)

        return all_vacancies_data

    def parse_workUa(self)->list:

        basepoint = 'https://www.work.ua'
        BASE_URL = 'https://www.work.ua/jobs-python/'
        page = 0

        with open('jobs.csv', 'w', encoding='UTF8') as f:

            writer = csv.writer(f)

            writer.writerow(('title', 'city', 'info', 'link'))
            while True:

                page += 1 

                params = {
                    'page': page
                }

                response = requests.get(BASE_URL, params=params, headers=self.headers)

                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')

                vacancies = soup.find_all('div', class_ = 'card card-hover card-visited wordwrap job-link')

                if len(vacancies) == 0:
                    break

                for vacancy in vacancies:

                    title =vacancy.find('h2').text.strip()
                    info = vacancy.find('p', class_ = 'overflow text-muted add-top-sm cut-bottom').text.strip()
                    link = basepoint + vacancy.find('a', class_ = 'no-decoration')['href']
                    # remote = vacancy.find('span', class_ = "icon icon-home_work").next_sibling.text.strip()

                    data = {'title': title, 'city': '', 'info': info, 'link': link, 'remote': ''}


        return 'all_vacancies_data'

