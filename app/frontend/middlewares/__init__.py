from aiogram import Dispatcher  # noqa

from main import bot  # noqa
from .throttling import ThrottlingMiddleware  # noqa

if __name__ == "middlewares":
    dp = bot.dp
    dp.middleware.setup(ThrottlingMiddleware())
