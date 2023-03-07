from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def my_favorites_keyboard(meme_now: int):
    favorites_kb = InlineKeyboardMarkup(row_width=3,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(text="Удалить",
                                                                     callback_data=f"delete_favorite_{meme_now}")
                                            ],
                                            [
                                                InlineKeyboardButton(text="<< Вернуться в меню",
                                                                     callback_data="del_returntomenu")
                                            ],
                                            [
                                                InlineKeyboardButton(text="Предыдущий",
                                                                     callback_data=f"show_previous_favorite_{meme_now - 1}"),
                                                InlineKeyboardButton(text="Следующий",
                                                                     callback_data=f"show_next_favorite_{meme_now + 1}")
                                            ]
                                        ])

    return favorites_kb
