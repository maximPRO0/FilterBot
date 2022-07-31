from loader import dp
from aiogram.types import CallbackQuery,Message
from aiogram.dispatcher import FSMContext
from sqlalchemy.orm import sessionmaker
from utils.db_api.db_gino import engine, Worlds
Session = sessionmaker()
from keyboards.inline.WordKeyboard import WorldKeyb
from states.AddWordState import Deletr
session = Session(bind=engine)

@dp.callback_query_handler(text='del')
async def del_word_db(call: CallbackQuery, state=None):
    await Deletr.step1.set()
    await call.message.answer("Qaysi so`zni ochirmoqchisiz?")
    await Deletr.next()


@dp.message_handler(state=Deletr.step2)
async def del_word(message: Message, state=FSMContext):
    text = message.text.lower()
    try:
        obj = session.query(Worlds).filter(Worlds.word == text).first()
        session.delete(obj)
        session.commit()
        await message.answer("So`z bazadan ochirilda\n"
                             "Menyu", reply_markup=WorldKeyb)
        print("|INFO| - BAZADAN SO`Z O`CHIRILDI!")
        await state.finish()
    except:
        print("|INFO| - BAZADA YO`Q SO`ZNI O`CHIRISHMOQCHI!")
        await message.answer("Kechirasiz, men bu so`zni bazadan topa-olmadim", reply_markup=WorldKeyb)
        await state.finish()
    finally:
        session.close()
