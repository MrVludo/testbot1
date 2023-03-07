import asyncio
import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data.config import admins
from keyboards.inline.create_meme_kb import create_meme_kb
from keyboards.inline.menu import menu
from loader import dp
from states.get_info import GetInfo
from utils.db_api.db_commands import create_row_memes, get_user_memes


@dp.callback_query_handler(Text(equals='create_meme'))
async def create_user_meme(call: types.CallbackQuery):
    data = await get_user_memes(telegram_id=call.from_user.id)

    meme_limit = 20 if str(call.from_user.id) not in admins else 1000

    if len(data) < meme_limit:
        await call.message.delete()
        await call.message.answer('Отправь мне мем', reply_markup=create_meme_kb)

        await GetInfo.photo.set()
    else:
        await call.answer("У вас не осталось свободных слотов. Купите премемим аккаунт!", show_alert=True)


@dp.message_handler(state=GetInfo.photo, content_types=types.ContentTypes.PHOTO)
async def get_photo_id(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await create_row_memes(telegram_id=message.from_user.id, photo_id=photo_id)

    await message.delete()

    await state.reset_state()

    await dp.bot.delete_message(message_id=message.message_id-1, chat_id=message.chat.id)

    success = await message.answer('Вы успешно создали мем!')
    await asyncio.sleep(2)
    await success.edit_text("Менюшка", reply_markup=menu)


@dp.callback_query_handler(Text(equals="stop_creating_meme"), state=GetInfo.photo)
async def creating_stop(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()

    await call.message.edit_text("Менюшка", reply_markup=menu)
