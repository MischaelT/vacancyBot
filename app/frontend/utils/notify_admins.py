import logging

from aiogram import Dispatcher

from frontend.data.dialogs import BOT_RUN

from settings.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, BOT_RUN)

        except Exception as err:
            logging.exception(err)
