from environs import Env

from backend.backend_manager import Backend_manager

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")


backend_manager = Backend_manager()