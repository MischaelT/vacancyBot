import logging

from aiogram.utils.exceptions import (CantParseEntities, MessageNotModified,
                                      MessageTextIsEmpty, TelegramAPIError)

from frontend.data.dialogs import NO_VACANCIES, NOT_MODIFIED_ERROR


async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks

    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, MessageNotModified):
        logging.exception(NOT_MODIFIED_ERROR)
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.exception(NO_VACANCIES)
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    #  MUST BE THE LAST CONDITION
    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    logging.exception(f'Update: {update} \n{exception}')
