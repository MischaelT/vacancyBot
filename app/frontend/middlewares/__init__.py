from aiogram import Dispatcher  # noqa

from .throttling import ThrottlingMiddleware  # noqa


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
