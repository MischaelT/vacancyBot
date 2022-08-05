from backend.data.db.choices import PYTHON
from backend.data.parser.sources.test_source import TestSource
from backend.backend_manager import Backend_manager
from frontend.bot import VacancyBot

backend_manager = Backend_manager()
bot = VacancyBot(backend_manager)


# parser = TestSource()





if __name__ == '__main__':
    bot.start()
    # parser.get_dev_vacancies(page=1, language=PYTHON,experience='no_exp')
    # print(parser.parsed_data)
