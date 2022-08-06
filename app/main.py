from backend.backend_manager import Backend_manager

from frontend.bot import VacancyBot

backend_manager = Backend_manager()
bot = VacancyBot(backend_manager)

if __name__ == '__main__':
    bot.start()
