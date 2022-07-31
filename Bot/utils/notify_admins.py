import logging

from aiogram import Dispatcher
from loader import bot

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=admin, text="|Launch|")

        except Exception as err:
            logging.exception(err)
