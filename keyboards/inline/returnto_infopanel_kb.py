from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

returnto_infopanel = InlineKeyboardMarkup(row_width=3,
                                          inline_keyboard=[[
                                              InlineKeyboardButton(text="<< Отменить", callback_data="show_info_panel")
                                          ]])