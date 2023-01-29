from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(row_width=3,
                            inline_keyboard=[[
                                InlineKeyboardButton(text="Информация пользователя", callback_data="show_info")
                            ],
                            [
                                InlineKeyboardButton(text="Смотреть мемы", callback_data="None")
                            ],
                            [
                                InlineKeyboardButton(text="Создать мем", callback_data="None"),
                                InlineKeyboardButton(text="Мои мемы", callback_data="None")
                            ],
                            [
                                InlineKeyboardButton(text="Избранное", callback_data="None")
                            ]]
                            )

