from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(row_width=3,
                            inline_keyboard=[[
                                InlineKeyboardButton(text="Информация пользователя", callback_data="show_info")
                            ],
                            [
                                InlineKeyboardButton(text="Смотреть мемы", callback_data="surfing_memes")
                            ],
                            [
                                InlineKeyboardButton(text="Создать мем", callback_data="create_meme"),
                                InlineKeyboardButton(text="Мои мемы", callback_data="show_meme")
                            ],
                            [
                                InlineKeyboardButton(text="Избранное", callback_data="surfing_favorites")
                            ]]
                            )

