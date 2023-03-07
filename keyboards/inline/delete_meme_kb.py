from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def my_memes_keyboard(meme_now: int):
    delete_meme_kb = InlineKeyboardMarkup(row_width=3,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text="Удалить", callback_data=f"delete_meme_{meme_now}")
                                              ],
                                              [
                                                  InlineKeyboardButton(text="<< Вернуться в меню",
                                                                       callback_data="del_returntomenu")
                                              ],
                                              [
                                                  InlineKeyboardButton(text="Предыдущий",
                                                                       callback_data=f"show_previous_meme_{meme_now - 1}"),
                                                  InlineKeyboardButton(text="Следующий",
                                                                       callback_data=f"show_next_meme_{meme_now + 1}")
                                              ]
                                          ])

    return delete_meme_kb
