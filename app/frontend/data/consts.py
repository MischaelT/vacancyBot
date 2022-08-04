from backend.data.db.choices import (ARCHITECT, CPLUSPLUS, INTERN, JAVA,
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

AREAS_LIST = {MANAGEMENT: 'Management' , DEVELOPMENT: 'Development' , DATA: 'Data Science', QA: 'QA' }
EXPERIENCES_LIST = {INTERN: '0-1' , JUNIOR:'1-2', MIDDLE:'2-4', SENIOR:'4-6', ARCHITECT:'6+'}
LANGUAGE_LIST = {PYTHON: 'Python',JAVA: 'Java' , CPLUSPLUS:'C++', SCALA:'Scala'}
CITIES_LIST = ['Odessa', 'Kyiv', 'Kharkiv', 'Lviv']
SALARIES_LIST = ['0-1000', '1000-2000', '3000-4000', '4000+']

QA_OPTIONS = ['Manual', 'Automation']
MANAGEMENT_OPTIONS = ['HR', 'PR']
DATA_OPTIONS = ['Analyst', 'Scientist', 'Engineer']
DEVELOPER_OPTIONS = ['Backend', 'Frontend']

SAVE_BUTTON = 'Save'
BACK_BUTTON = 'Back'
