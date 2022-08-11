from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandHelp, CommandStart

from frontend.handlers.users.admin import show_admin_panel
from frontend.handlers.dialogs.dialog_structure import dialog_structure
from frontend.handlers.users.get_vacancies import get_vacancies
from frontend.keyboards.inline.settings_keyboards import menu_cd
from frontend.utils.states.settings_states import UserSettings

from .help import bot_help
from ..dialogs.main_handler import settings_menu
from ..dialogs.setUp_settings_handler import (area_menu, data_menu, developer_menu,
                                     experience_menu, language_menu,
                                     location_menu, management_menu, qa_menu,
                                     salary_menu, save_menu, save_process)
from .start import bot_start


def setup(dp: Dispatcher):

    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())

    dp.register_message_handler(get_vacancies, commands=['vacancies'], state=None)
    dp.register_message_handler(settings_menu, commands=['settings'], state=None)
    dp.register_message_handler(show_admin_panel, commands=['admin'], state=None)

    dp.register_callback_query_handler(area_menu, state=UserSettings.area)
    dp.register_callback_query_handler(experience_menu, state=UserSettings.experience)

    dp.register_callback_query_handler(data_menu, state=UserSettings.data)
    dp.register_callback_query_handler(qa_menu, state=UserSettings.qa)
    dp.register_callback_query_handler(developer_menu, state=UserSettings.developer)
    dp.register_callback_query_handler(management_menu, state=UserSettings.management)

    dp.register_callback_query_handler(language_menu, state=UserSettings.language)
    dp.register_callback_query_handler(location_menu, state=UserSettings.location)
    dp.register_callback_query_handler(salary_menu, state=UserSettings.salary)

    dp.register_callback_query_handler(save_menu, state=UserSettings.save)
    dp.register_callback_query_handler(save_process, state=UserSettings.save_process)

    dp.register_callback_query_handler(dialog_structure, menu_cd.filter())
