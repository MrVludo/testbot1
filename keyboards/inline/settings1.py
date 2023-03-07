from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

settings1 = InlineKeyboardMarkup(row_width=3,
                                 inline_keyboard=[[
                                     InlineKeyboardButton(text='Изменить на: Да', callback_data='settingstoTrue')
                                 ], [
                                     InlineKeyboardButton(text='<< Вернуться', callback_data='returnto_infomenu')
                                 ]])


async def settings_keyboard(status):

    keyboard = InlineKeyboardMarkup(row_width=3)

    if status:
        keyboard.add(InlineKeyboardButton(text='Изменить на: Нет', callback_data='settings_to_False'))
    else:
        keyboard.add(InlineKeyboardButton(text='Изменить на: Да', callback_data='settings_to_True'))

    keyboard.add(InlineKeyboardButton(text='<< Вернуться', callback_data='returnto_infomenu'))

    return keyboard

