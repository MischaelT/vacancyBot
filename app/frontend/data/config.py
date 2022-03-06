# import random
from backend.backend_manager import Backend_manager

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")


backend_manager = Backend_manager()

# is_registered = bool(random.getrandbits(1))

is_registered = False
