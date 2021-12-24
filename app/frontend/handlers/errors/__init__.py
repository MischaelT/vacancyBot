from .error_handler import errors_handler # noqa
from aiogram import Dispatcher

def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
