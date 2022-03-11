import asyncio
import random
from asyncio.events import new_event_loop, set_event_loop

import requests
from backend.data.vacancy_data_manager import Vacancies_manager
from backend.data.parser.consts import (DATA, djinni_exp_levels,
                                        djinni_languages, dou_exp_levels,
                                        dou_languages)
from backend.data.parser.parser import parse_djinni_data, parse_dou_data


class ParseManager:

    def __init__(self, vacancy_manager) -> None:

        self.vacancy_manager = vacancy_manager
        self.headers = {'User-Agent': ''}
        self.proxy = {'http': 'http//:'}

        with open('proxies.txt', 'r') as f:
            self.proxies_list = f.read().split('\n')

        with open('user-agents.txt', 'r') as f:
            self.user_agents_list = f.read().split('\n')


    async def run_general_parsing(self) -> None:

        loop = new_event_loop()
        set_event_loop(loop)

        page = 0

        while True:

            page += 1

            tasks = self.__add_tasks(page)

            await asyncio.gather(*tasks, return_exceptions=True)

            if page == 1:
                break

        print('end_parsing')


    def __add_tasks(self, page: int) -> list:

        tasks = []

        for language in djinni_languages:
            for exp in djinni_exp_levels:

                task = asyncio.ensure_future(self.__get_djinni_content(page, language, exp))
                tasks.append(task)
        
        # for language in dou_languages:
        #     for exp in dou_exp_levels:

        #         task = asyncio.ensure_future(self.__get_dou_content(page, language, exp))
        #         tasks.append(task)

        # print(tasks)

        return tasks


    async def __get_djinni_content(self, page: int, language: dict, experience: dict):

        print('parse djinni', language, experience)

        self.headers['User-Agent'] = random.choice(self.user_agents_list)
        self.proxy['http'] += random.choice(self.proxies_list)

        settings = DATA.get('djinni')

        basepoint = settings.get('basepoint')
        endpoint = settings.get('endpoint')
        params = settings.get('params')

        # params['page'] = page
        print(experience.keys())

        params['exp_level'] = list(experience.keys())[0]
        params['keywords'] = list(language.keys())[0]

        await asyncio.sleep(random.uniform(5, 10))

        response = requests.get(basepoint+endpoint, headers=self.headers, params=params, proxies=self.proxy)
        response.raise_for_status()

        await parse_djinni_data(self.vacancy_manager ,response.text, basepoint=basepoint, language=list(language.values())[0], experience=list(experience.values())[0])


    async def __get_dou_content(self, page: int, language: str, experience: str):

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

        await asyncio.sleep(random.uniform(10, 20))
