from aiogram import types

from frontend.data.dialogs import GET_HELP, RUN_BOT


async def bot_help(message: types.Message):

    text = ("Command list: ",
            f"/start - {RUN_BOT}",
            f"/help - {GET_HELP}")

    await message.answer("\n".join(text))
