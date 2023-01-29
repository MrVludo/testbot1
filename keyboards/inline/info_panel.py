from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

info_panel = InlineKeyboardMarkup(row_width=3,
                                  inline_keyboard=[[
                                      InlineKeyboardButton(text='Изменить имя', callback_data='change_name')
                                  ],
                                  [
                                      InlineKeyboardButton(text='Изменить описание', callback_data='change_description')
                                  ],
                                  [
                                      InlineKeyboardButton(text='<< Вернуться', callback_data='returnto_infomenu')
                                  ]
                                  ])
