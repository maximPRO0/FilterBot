from aiogram.dispatcher.filters.builtin import CommandStart
from sqlalchemy.orm import sessionmaker

from loader import dp
from aiogram.types import Message
from utils.db_api.db_gino import engine, session, User
Session = sessionmaker(bind=engine)




@dp.message_handler(CommandStart())
async def cmd_start(message: Message):
    session = Session(bind=engine)
    try:
        user = User(full_name=message.from_user.full_name,
                    username=message.from_user.username,
                    user_id=message.from_user.id)
        session.add(user)
        session.commit()
        await message.answer(f"Assalom aleykum {message.from_user.full_name}\n"
                             f"Sizni ilk bora ko`rib turganimdan xursandman")
        print(f"|INFO|- {message.from_user.full_name.upper()} BAZAGA QO`SHILDI!")
    except:
        session.rollback()
        await message.answer(f"Salom {message.from_user.first_name}, sizni ko`rib turganimdan xursandman")
        print(f"|INFO| - {message.from_user.full_name.upper()} BAZADA MAVJUD!! ")

    finally:
        session.close()

