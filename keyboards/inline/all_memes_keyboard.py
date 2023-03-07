from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def all_memes_keyboard(meme_now: int):
    all_memes_kb = InlineKeyboardMarkup(row_width=3,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(text="<< Вернуться в меню",
                                                                     callback_data="del_returntomenu")
                                            ],
                                            [
                                                InlineKeyboardButton(text="🔥 Добавить в избранное 🔥", callback_data=f"add_to_favorites_{meme_now}")
                                            ],
                                            [
                                                InlineKeyboardButton(text="Следующий",
                                                                     callback_data=f"surfing_memes_{meme_now}")
                                            ]
                                        ])

    return all_memes_kb
