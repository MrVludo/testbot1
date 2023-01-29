import time

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.inline.menu import menu
from loader import dp
from utils.db_api.db_commands import create_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username
    )
    await message.answer('Привет! Я бот Серафим! Можешь звать меня МемПлэйсБот :)')
    #time.sleep(2)
    await message.answer('Менюшка', reply_markup=menu)

