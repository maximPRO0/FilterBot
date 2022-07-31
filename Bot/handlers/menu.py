from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message
from keyboards.inline.WordKeyboard import WorldKeyb
from data.config import ADMINS
from loader import dp

global admin
for admin in ADMINS:
    pass


@dp.message_handler(Command("add", prefixes="/"), chat_id=admin)
async def settingwords(message: Message):
    await message.answer("Menu", reply_markup=WorldKeyb)
