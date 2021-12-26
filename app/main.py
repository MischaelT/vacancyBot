from backend.app_flow_manager import AppFlow_manager
from frontend.bot import VacancyBot

bot = VacancyBot()

flow_manager = AppFlow_manager(bot)


if __name__ == '__main__':
    bot.start()  
    flow_manager.run()
