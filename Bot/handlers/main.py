from loader import dp
from aiogram.types import Message
from filters import IsGroup
from sqlalchemy.orm import sessionmaker
from utils.db_api.db_gino import engine, Worlds
Session = sessionmaker()
session = Session(bind=engine)

@dp.message_handler(IsGroup())
async def cmd_all(message: Message):
    text = message.text.lower()
    result = session.query(Worlds.word).all()
    # print(result)
    for uwu in result:
        if text in uwu[0]:
            await message.delete()
            await message.answer(f"{message.from_user.full_name} Siz bazadagi taqiqlangan so`zni ishlatingiz!\n"
                                 f"Iltimos guruh qoidalariga rioya qiling!")
        else:
            pass

    # x = ['']
    # global i
    # for i in result:
    #     x.append(i[0])

    # a = "\n".join(x)
    # print(message.text)
    # print(a)
    # res = a in message.text
    # print(res)
    # if res == True:
    #     await message.delete()
    #     await message.answer(f"{message.from_user.full_name} Siz taqiqlangan so`z yozdingiz\n"
    #                              f"Iltimos guruh qoidalarini buzmang!")
    #     print(f"|INFO|- {message.from_user.full_name} НАПИСАЛ ЗАПРЕЩЕННОЕ СЛОВО")
    # else:
    #     pass

