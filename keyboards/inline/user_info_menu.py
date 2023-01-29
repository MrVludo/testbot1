from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

user_info_menu = InlineKeyboardMarkup(row_width=3,
                                      inline_keyboard=[[
                                          InlineKeyboardButton(text='Имя, описание', callback_data='show_info_panel')
                                      ],
                                      [
                                          InlineKeyboardButton(text='Настройки', callback_data='show_settings')
                                      ],
                                      [
                                          InlineKeyboardButton(text='<< Назад в меню', callback_data='returntomenu')
                                      ]
                                      ])