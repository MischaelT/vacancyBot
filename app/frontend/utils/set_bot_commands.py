from aiogram import Dispatcher, types

from frontend.data.dialogs import BOT_STARTED, HELP


async def set_default_commands(dp: Dispatcher):

    """
        Function sets default commands
    """

    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", BOT_STARTED),
            types.BotCommand("help", HELP),
        ]
    )
