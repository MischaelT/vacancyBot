from backend.backend_manager import BackendManager

from frontend.bot import VacancyBot

backend_manager = BackendManager()
bot = VacancyBot(backend_manager)

import logging
from backend.data.parser.sources.test_source import TestSource  


if __name__ == '__main__':
    bot.start()
    # parser = TestSource()
    # parser.get_content(page=1,language='Python', experience='0-1')
    # print(parser.parsed_data)


    # for vacancy in parser.parsed_data:
        # print(vacancy.title)
        # print(vacancy.info)
        # print(vacancy.language)
    
