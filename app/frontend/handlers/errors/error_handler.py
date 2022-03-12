import logging

from aiogram.utils.exceptions import (CantParseEntities,
                                      MessageNotModified,
                                      TelegramAPIError,
                                      MessageTextIsEmpty
                                      )


async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks
    
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, MessageNotModified):
        logging.exception('Message is not modified')
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.exception('There is no vacancies by that request')
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    #  MUST BE THE  LAST CONDITION 
    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True


    logging.exception(f'Update: {update} \n{exception}')
