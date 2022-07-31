from utils.db_api.db_gino import conn, words, meta

from sqlalchemy import delete, Table

b = Table('Worlds', meta, autoload=True)
a = b.delete().where(b.c.word=='krisa')
conn.execute(a)