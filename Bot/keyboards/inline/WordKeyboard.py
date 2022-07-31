from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

WorldKeyb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="So`z qo`shish", callback_data="add"),
            InlineKeyboardButton(text="So`zni o`chirish", callback_data="del"),
            InlineKeyboardButton(text="Barcha so`zlar", callback_data="all")
        ]
    ]
)