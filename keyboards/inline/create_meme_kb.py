from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

create_meme_kb = InlineKeyboardMarkup(row_width=3,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text="<< Отмена", callback_data="stop_creating_meme")
                                          ]
                                      ])
