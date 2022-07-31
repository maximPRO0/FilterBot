from aiogram.types import CallbackQuery, Message
from loader import dp
from aiogram.dispatcher import FSMContext
from states.AddWordState import Adder
from sqlalchemy.orm import sessionmaker
from utils.db_api.db_gino import engine, Worlds
Session = sessionmaker()
session = Session(bind=engine)



@dp.callback_query_handler(text='add')
async def add_word_db(call : CallbackQuery, state=None):
    await Adder.step1.set()
    await call.message.reply("Marxamat so`zni kiriting: ")
    await Adder.next()

@dp.message_handler(state=Adder.step2)
async def add(message: Message, state: FSMContext):
    session = Session(bind=engine)
    try:
        word = Worlds(word=message.text.lower())
        session.add(word)
        session.commit()
        await message.answer("So`zni bazaga qo`shdim!")
        print("|INFO| - ADDED NEW WORD")
        await state.finish()
    except:
        session.rollback()
        await message.answer("Kechirasiz, bu so`z bazada mavjud!")
        print("|INFO| BAZADA BOR SO`ZNI QOSHMOQCHI BO`LISHDI")
        await state.finish()
    finally:
        session.close()