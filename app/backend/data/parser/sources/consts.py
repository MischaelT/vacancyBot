from backend.data.db.choices import ARCHITECT, CPLUSPLUS, HR, INTERN, JAVA, JUNIOR, MIDDLE, PM, PYTHON, SCALA, SENIOR

DJINNI_DATA = {
    'djinni_exp_levels': {'no_exp': INTERN, '1y': JUNIOR, '2y': MIDDLE, '3y': MIDDLE, '5y': ARCHITECT},
    'djinni_languages': {'python': PYTHON, 'java': JAVA, 'scala': SCALA, 'cplusplus': CPLUSPLUS},
    'root': 'https://djinni.co',
    'basepoint': '/jobs/',
    'non_dev_endpoint': 'keyword-',
    'non_dev_positions': {'project-manager': PM, 'hr': HR}
}

DOU_DATA = {
    'dou_exp_levels': {'0-1': JUNIOR, '1-3': MIDDLE, '3-5': SENIOR, '5plus': ARCHITECT},
    'dou_languages': {'Python': PYTHON, 'Scala': SCALA, 'Java': JAVA},
    'root': 'https://jobs.dou.ua',
    'basepoint': '/vacancies/',
    'non_dev_endpoint': '',
    'non_dev_positions': ''
}

WORKUA_DATA = {
    'dou_exp_levels': '',
    'dou_languages': {'python': PYTHON, 'java': JAVA, 'scala': SCALA, 'c%2B%2B': CPLUSPLUS},
    'root': 'https://www.work.ua',
    'basepoint': '',
    'non_dev_endpoint': '',
    'non_dev_positions': ''
}
