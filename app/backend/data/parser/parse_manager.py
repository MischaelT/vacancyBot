import asyncio
import random
from asyncio.events import new_event_loop, set_event_loop

import requests
from backend.data.parser.consts import (DATA, djinni_exp_levels,
                                        djinni_languages, dou_exp_levels,
                                        dou_languages)
from backend.data.parser.parsers import parse_djinni_data, parse_dou_data


class ParseManager:

    """
        Class that provides methods for parsing data
    """    

    def __init__(self, vacancy_manager) -> None:

        self.vacancy_manager = vacancy_manager
        self.headers = {'User-Agent': ''}
        self.proxy = {'http': 'http//:'}

        with open('proxies.txt', 'r') as f:
            self.proxies_list = f.read().split('\n')

        with open('user-agents.txt', 'r') as f:
            self.user_agents_list = f.read().split('\n')


    async def run_general_parsing(self) -> None:

        """
            Method run parsing for every page
        """        

        loop = new_event_loop()
        set_event_loop(loop)

        page = 0

        while True:

            page += 1

            tasks = self.__add_tasks(page)

            await asyncio.gather(*tasks, return_exceptions=True)

            if page == 1:
                break


    def __add_tasks(self, page: int) -> list:

        """
            Method generates list of asyncio tasks.
            Randomly adds asyncio.sleep() task to be polite to server

        Returns:
            list: task list
        """        

        tasks = []

        for language in djinni_languages:
            for exp in djinni_exp_levels:

                task = asyncio.ensure_future(self.__get_djinni_content(page, language, exp))
                tasks.append(task)

                if bool(random.getrandbits(1)):
                    task = asyncio.sleep(random.uniform(3, 6))
                    tasks.append(task)
        
        for language in dou_languages:
            for exp in dou_exp_levels:

                task = asyncio.ensure_future(self.__get_dou_content(page, language, exp))
                tasks.append(task)

                if bool(random.getrandbits(1)):
                    task = asyncio.sleep(random.uniform(3, 6))
                    tasks.append(task)

        return tasks


    async def __get_djinni_content(self, page: int, language: dict, experience: dict):

        """
        Method connects to djinni.ua and get information. 
        Then call function parse_djinni_data()

        Args:
            page (int): page for parsing
            language (dict): language for params
            experience (dict): experience for params
        """      

        print('parse djinni', language, experience)

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

        parse_djinni_data(self.vacancy_manager ,response.text, basepoint=basepoint, language=list(language.values())[0], experience=list(experience.values())[0])


    async def __get_dou_content(self, page: int, language: str, experience: str):
        """
            Method connects to djinni.ua and get information. 
            Then call function parse_djinni_data()

        Args:
            page (int): page for parsing
            language (str): language for params
            experience (str): eperience for params
        """

        print('parse dou', language, experience)

        self.headers['User-Agent'] = random.choice(self.user_agents_list)
        self.proxy['http'] += random.choice(self.proxies_list)

        settings = DATA.get('dou')

        basepoint = settings.get('basepoint')
        endpoint = settings.get('endpoint')
        params = settings.get('params')

        params['page'] = page

        params['exp'] = experience
        params['category'] = language

        response = requests.get(basepoint+endpoint, headers=self.headers, params=params, proxies=self.proxy)
        response.raise_for_status()

        vacancies_data = await parse_dou_data(response.text)
        details = {'language': language, 'experience': experience}
        vacancies_data.append(details)
