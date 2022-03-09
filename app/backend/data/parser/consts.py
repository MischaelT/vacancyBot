djinni_exp_levels = ['no_exp', '1y', '2y', '3y', '5y']
djinni_languages = ['python', 'java', 'scala', 'cplusplus']

dou_exp_levels = ['0-1', '1-3', '3-5', '5plus']
dou_languages = ['Python', 'Scala', 'Java', 'C%2B%2B']

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
