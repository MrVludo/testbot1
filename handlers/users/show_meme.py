import time

from aiogram import types
from aiogram.dispatcher.filters import Text

from data.config import admins
from keyboards.inline.delete_meme_kb import my_memes_keyboard
from keyboards.inline.menu import menu
from loader import dp
from utils.db_api.db_commands import get_user_memes, delete_user_meme


@dp.callback_query_handler(Text(startswith='delete_meme'))
async def delete_user_memes(call: types.CallbackQuery):
    data = await get_user_memes(telegram_id=call.from_user.id)
    meme_now = int(call.data.split('_')[2])

    await delete_user_meme(data[meme_now].photo_id)

    await call.answer("Мем удалён!")

    await call.message.delete()

    await call.message.answer(text="Менюшка:", reply_markup=menu)


@dp.callback_query_handler(Text(equals='show_meme'))
async def show_user_memes(call: types.CallbackQuery):
    meme_limit = 20 if str(call.from_user.id) not in admins else 1000

    data = await get_user_memes(telegram_id=call.from_user.id)
    if len(data) > 0:
        await call.message.delete()
        keyboard = await my_memes_keyboard(meme_now=0)
        await call.message.answer_photo(
            photo=data[0].photo_id,
            caption=f"Слот {str(1)}/{len(data)} (max. {meme_limit})",
            reply_markup=keyboard
        )

    else:
        await call.answer("Создайте сначала что нибудь!")


@dp.callback_query_handler(Text(startswith='show_next_meme'))
async def show_next_user_memes(call: types.CallbackQuery):
    meme_limit = 20 if str(call.from_user.id) not in admins else 1000

    data = await get_user_memes(telegram_id=call.from_user.id)
    meme_now = int(call.data.split('_')[3])

    if len(data) > meme_now:
        keyboard = await my_memes_keyboard(meme_now=meme_now)
        await call.message.delete()

        await call.message.answer_photo(
            photo=data[meme_now].photo_id,
            caption=f"Слот {str(meme_now+1)}/{len(data)} (max. {meme_limit})",
            reply_markup=keyboard
        )

    else:
        msg = await call.answer("Это всё!")


@dp.callback_query_handler(Text(startswith='show_previous_meme'))
async def show_next_user_memes(call: types.CallbackQuery):
    meme_limit = 20 if str(call.from_user.id) not in admins else 1000

    data = await get_user_memes(telegram_id=call.from_user.id)
    meme_now = int(call.data.split('_')[3])
    if meme_now < 0:
        meme_now = 0
    await call.message.delete()
    keyboard = await my_memes_keyboard(meme_now=meme_now)
    await call.message.answer_photo(
        photo=data[meme_now].photo_id,
        caption=f"Слот {str(meme_now+1)}/{len(data)} (max. {meme_limit})",
        reply_markup=keyboard
    )
