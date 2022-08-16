import enum

from backend.data.db.choices import (ANALYST, ARCHITECT, AUTO, BACKEND,
                                     CPLUSPLUS, DATA, DEVELOPMENT, ENGINEER,
                                     FRONTEND, HR, INTERN, JAVA, JUNIOR,
                                     MANAGEMENT, MANUAL, MIDDLE, PM, PYTHON,
                                     QA, SCALA, SCIENTIST, SENIOR)

from frontend.data.buttons import (ANALYST_BUTTON, ARCHITECT_BUTTON,
                                   AUTOMATION_BUTTON, BACKEND_BUTTON,
                                   CHANGE_SETTINGS_BUTTON, CPLUSPLUS_BUTTON,
                                   DATA_BUTTON, DEVELOPMENT_BUTTON,
                                   ENGINEER_BUTTON, FRONTEND_BUTTON,
                                   GET_USERS_BUTTON, GET_VACANCIES_BUTTON,
                                   HR_BUTTON, INTERN_BUTTON, JAVA_BUTTON,
                                   JUNIOR_BUTTON, KHARKIV_BUTTON, KYIV_BUTTON,
                                   LVIV_BUTTON, MANAGEMENT_BUTTON,
                                   MANUAL_BUTTON, MIDDLE_BUTTON,
                                   MY_SETTINGS_BUTTON, ODESSA_BUTTON,
                                   PM_BUTTON, PYTHON_BUTTON, QA_BUTTON,
                                   RUN_PARSING_BUTTON, SALARY_0_1000_BUTTON,
                                   SALARY_1000_2000_BUTTON, SALARY_3000_4000_BUTTON,
                                   SALARY_4000_PLUS_BUTTON, SCALA_BUTTON,
                                   SCIENTIST_BUTTON, SENIOR_BUTTON,
                                   SETTINGS_BUTTON)


# TODO  add 8, 9 admin functions
class Callbacks(enum.Enum):
    main = 1
    get_vacancies = 2
    settings = 3
    my_settings = 4
    admin = 5
    run_parsing = 6
    get_users = 7
    choose_area = 10
    area_management = 11
    area_ds = 12
    area_qa = 13
    area_dev = 14


MAIN_MENU_LIST = [GET_VACANCIES_BUTTON, SETTINGS_BUTTON]
SETTINGS_MENU_LIST = [MY_SETTINGS_BUTTON, CHANGE_SETTINGS_BUTTON]
CITIES_LIST = [ODESSA_BUTTON, KYIV_BUTTON, LVIV_BUTTON, KHARKIV_BUTTON]
SALARIES_LIST = [SALARY_0_1000_BUTTON, SALARY_1000_2000_BUTTON, SALARY_3000_4000_BUTTON, SALARY_4000_PLUS_BUTTON]
AREAS_LIST = {MANAGEMENT: MANAGEMENT_BUTTON, DEVELOPMENT: DEVELOPMENT_BUTTON, DATA: DATA_BUTTON, QA: QA_BUTTON}
EXPERIENCES_LIST = {INTERN: INTERN_BUTTON, JUNIOR: JUNIOR_BUTTON, MIDDLE: MIDDLE_BUTTON, SENIOR: SENIOR_BUTTON, ARCHITECT: ARCHITECT_BUTTON}
LANGUAGE_LIST = {PYTHON: PYTHON_BUTTON, JAVA: JAVA_BUTTON, CPLUSPLUS: CPLUSPLUS_BUTTON, SCALA: SCALA_BUTTON}
ADMIN_MENU_LIST = [RUN_PARSING_BUTTON, GET_USERS_BUTTON]


QA_OPTIONS = {MANUAL: MANUAL_BUTTON, AUTO: AUTOMATION_BUTTON}
MANAGEMENT_OPTIONS = {HR: HR_BUTTON, PM: PM_BUTTON}
DATA_OPTIONS = {ANALYST: ANALYST_BUTTON, SCIENTIST: SCIENTIST_BUTTON, ENGINEER: ENGINEER_BUTTON}
DEVELOPER_OPTIONS = {BACKEND: BACKEND_BUTTON, FRONTEND: FRONTEND_BUTTON}
