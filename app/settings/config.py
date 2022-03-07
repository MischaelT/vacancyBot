from pathlib import Path

from backend.backend_manager import Backend_manager

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

REDIS_PASSWORD = env.str('REDIS_PASSWORD')
REDIS_HOST = env.str('REDIS_HOST')
REDIS_PORT = env.str('REDIS_PORT')

BASE_DIR = Path(__file__).resolve().parent.parent


POSTGRES_USER = env.str('POSTGRES_USER')
POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD')
POSTGRES_HOST = env.str('POSTGRES_HOST')
POSTGRES_PORT = env.str('POSTGRES_PORT')
POSTGRES_DB = env.str('POSTGRES_DB')

is_registered = False

# CELERY_BROKER_URL = 'amqp://rabbitmq'

# CELERY_BEAT_SCHEDULE = {
#
# }

DATABASES = {
    'default': {
        'NAME': 'sqlite3',
        'PATH': BASE_DIR/'vacancies.db',
    },

    'production': {
        #  'NAME': 'postgresql',
        # 'PATH': os.environ['POSTGRES_DB'],
        #  'USER': os.environ['POSTGRES_USER'],
        #  'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        #  'HOST': os.environ['POSTGRES_HOST'],
        #  'PORT': os.environ['POSTGRES_PORT'],
    }

}

backend_manager = Backend_manager()
