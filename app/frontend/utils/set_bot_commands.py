from aiogram import Dispatcher, types


async def set_default_commands(dp:Dispatcher):

    """
        Function sets default commands
    """

    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start bot"),
            types.BotCommand("help", "Help"),
        ]
    )
