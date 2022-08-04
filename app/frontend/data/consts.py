from backend.data.db.choices import (ARCHITECT, CPLUSPLUS, ENGLISH, INTERN, JAVA,
                                     JUNIOR, MIDDLE, PYTHON, SCALA, SENIOR, DEVELOPMENT, MANAGEMENT, DATA, QA)

MAIN_MENU = 1
GET_VACANCIES_MENU = 2
SETTINGS_MENU = 3
MY_SETTINGS = 4

CHOOSE_AREA = 10
AREA_MANAGEMENT = 11
AREA_DS = 12
AREA_DEVELOPER = 14
AREA_QA = 13


SETTINGS_MENU_LIST = ['My settings', 'Change settings']

AREAS_LIST = {'Management': MANAGEMENT, 'Development': DEVELOPMENT, 'Data Science': DATA, 'QA': QA}
EXPERIENCES_LIST = {'0-1': INTERN, '1-2': JUNIOR, '2-4': MIDDLE, '4-6': SENIOR, '6+': ARCHITECT}
CITIES_LIST = ['Odessa', 'Kyiv', 'Kharkiv', 'Lviv']
SALARIES_LIST = ['0-1000', '1000-2000', '3000-4000', '4000+']

LANGUAGE_LIST = {'Python': PYTHON, 'Java': JAVA, 'C++': CPLUSPLUS, 'Scala': SCALA}


QA_OPTIONS = ['Manual', 'Automation']
MANAGEMENT_OPTIONS = ['HR', 'PR']
DATA_OPTIONS = ['Analyst', 'Scientist', 'Engineer']
DEVELOPER_OPTIONS = ['Backend', 'Frontend']


SAVE_BUTTON = 'Save'
BACK_BUTTON = 'Back'
CONTINUE_BUTTON = 'Continue'
