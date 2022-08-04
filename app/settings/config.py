from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

REDIS_PASSWORD = env.str('REDIS_PASSWORD')
REDIS_HOST = env.str('REDIS_HOST')
REDIS_PORT = env.str('REDIS_PORT')

POSTGRES_USER = env.str('POSTGRES_USER')
POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD')
POSTGRES_HOST = env.str('POSTGRES_HOST')
POSTGRES_PORT = env.str('POSTGRES_PORT')
POSTGRES_DB = env.str('POSTGRES_DB')

