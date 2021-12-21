from app_flow_manager import appFlow_manager
# from frontend.bot import VacancyBot

# bot = VacancyBot()

flow_manager = appFlow_manager()


if __name__ == '__main__':
    # dp = bot.dp
    flow_manager.start()
