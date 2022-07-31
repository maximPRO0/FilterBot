from environs import Env
env = Env()
env.read_env()


ADMINS = env.list("ADMINS")
BOT_TOKEN = env.str("BOT_TOKEN")
Ip = env.str("IP")
PGUSER = env.str("PGUSER")
PGPASS = env.str("PGPASS")
DATABASE = env.str("DATABASE")

POSTGRESURI = f'postgresql://{PGUSER}:{PGPASS}@{Ip}/{DATABASE}'