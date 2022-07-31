from loader import dp
from aiogram.types import CallbackQuery
from sqlalchemy.orm import sessionmaker
from utils.db_api.db_gino import engine, Worlds
Session = sessionmaker()
session = Session(bind=engine)

@dp.callback_query_handler(text='all')
async def cmd_all(call: CallbackQuery):
    x = ['']
    result = session.query(Worlds.word).all()
    for i in result:
        x.append(i[0])
    a = "\n".join(x)

    await call.message.answer(f"Bazada mavjud so`zlar: {a}")