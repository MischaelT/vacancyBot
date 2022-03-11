from backend.data.parser.choices import ARCHITECT, CPLUSPLUS, JAVA, JUNIOR, MIDLLE, PYTHON, SCALA, SENIOR


djinni_exp_levels = [{'no_exp': JUNIOR}, {'1y': JUNIOR}, {'2y': MIDLLE}, {'3y': SENIOR}, {'5y':ARCHITECT}]
djinni_languages = [{'python': PYTHON}, {'java': JAVA}, {'scala': SCALA}, {'cplusplus': CPLUSPLUS}]

dou_exp_levels = [{'0-1': JUNIOR}, {'1-3': MIDLLE}, {'3-5': SENIOR}, {'5plus': ARCHITECT}]
dou_languages = [{'Python': PYTHON}, {'Scala': SCALA}, {'Java': JAVA}]  # 'C%2B%2B'

workUa_languages = ['python', 'java', 'scala', 'c%2B%2B']


DATA = {
    'dou': {
            'basepoint': 'http://jobs.dou.ua',
            'endpoint': '/vacancies/',
            'params': {
                        'category': '',
                        'exp': '',
                    },
    },
    'djinni': {
        'basepoint': 'https://djinni.co',
        'endpoint': '/jobs/',
        'params': {
                    'keywords': '',
                    'exp_level': '',

                }
    },
    'work': {
        'basepoint': 'https://www.work.ua',
        'endpoint': '/jobs-python/',
        'params': {},
    }
}
