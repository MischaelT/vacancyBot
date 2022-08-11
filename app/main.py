from backend.backend_manager import BackendManager

from frontend.bot import VacancyBot

backend_manager = BackendManager()
bot = VacancyBot(backend_manager)

if __name__ == '__main__':
    bot.start()
