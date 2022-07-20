import asyncio
import logging
import random
from asyncio.events import new_event_loop, set_event_loop
from backend.data.parsers.sources.djinni_source import DjinniSource
from backend.data.parsers.sources.dou_source import DouSource

from backend.data.parsers.consts import (DATA, djinni_exp_levels,
                                        djinni_languages, dou_exp_levels,
                                        dou_languages)


import requests


class ParseManager:

    """
        Class that provides methods for parsing data
    """

    def __init__(self, vacancy_manager) -> None:

        self.vacancy_manager = vacancy_manager

        self.djinni = DjinniSource(self.vacancy_manager)
        self.dou = DouSource(self.vacancy_manager)

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

        func_list = self.dou.make_futures(page=page)

        for function in func_list:

            task = asyncio.ensure_future(function)
            tasks.append(task)

            if bool(random.getrandbits(1)):
                task = asyncio.sleep(random.uniform(3, 6))
                tasks.append(task)

        # func_list = self.djinni.make_futures(page=page)

        # for function in func_list:

        #     task = asyncio.ensure_future(function)
        #     tasks.append(task)

        #     if bool(random.getrandbits(1)):
        #         task = asyncio.sleep(random.uniform(3, 6))
        #         tasks.append(task)

        return tasks


