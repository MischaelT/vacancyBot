import asyncio
import logging
import random
from asyncio.events import new_event_loop, set_event_loop

from backend.data.parser.sources.djinni_source import DjinniSource
from backend.data.parser.sources.dou_source import DouSource


class ParseManager:

    """
        Class that provides methods for parsing data
    """

    def __init__(self) -> None:

        self.djinni = DjinniSource()
        self.dou = DouSource()

    async def run_general_parsing(self) -> list:

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

        parsed_data = self.djinni.parsed_data + self.dou.parsed_data

        logging.debug('Parsing')

        return parsed_data

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

        func_list = self.djinni.make_futures(page=page)

        for function in func_list:

            task = asyncio.ensure_future(function)
            tasks.append(task)

            if bool(random.getrandbits(1)):
                task = asyncio.sleep(random.uniform(3, 6))
                tasks.append(task)

        return tasks
