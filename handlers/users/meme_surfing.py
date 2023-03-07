import random
from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.all_memes_keyboard import all_memes_keyboard
from loader import dp
from utils.db_api.db_commands import get_all_memes, select_user


@dp.callback_query_handler(Text(startswith='surfing_memes'))
async def surfing(call: types.CallbackQuery):

    all_all_memes = await get_all_memes()
    all_memes = []

    for i in all_all_memes:
        if i.user.settings:
            all_memes.append(i)

    if len(call.data.split('_')) == 2:

        if len(all_memes) > 0:
            meme_now = random.randint(0, len(all_memes) - 1)
            await call.message.delete()
            keyboard = await all_memes_keyboard(meme_now=meme_now)
            await call.message.answer_photo(
                photo=all_memes[meme_now].photo_id,
                caption=f"От: {all_memes[meme_now].user.nickname}",
                reply_markup=keyboard
            )

        else:
            await call.answer("Никто пока мемов не делал :(")

    else:

        if len(all_memes) > 1:
            meme_now = random.randint(0, len(all_memes) - 1)

            while meme_now == int(call.data.split('_')[2]):
                meme_now = random.randint(0, len(all_memes)-1)

            await call.message.delete()
            keyboard = await all_memes_keyboard(meme_now=meme_now)
            await call.message.answer_photo(
                photo=all_memes[meme_now].photo_id,
                caption=f"От: {all_memes[meme_now].user.nickname}",
                reply_markup=keyboard
            )

        else:
            await call.answer("Это всё! :(")
"""
@dp.callback_query_handler(Text(startswith='show_next_global_meme'))
async def show_next_user_memes(call: types.CallbackQuery):
    all_memes = await get_all_memes()
    
    meme_now = int(call.data.split('_')[4])

    if len(all_memes) > meme_now:
        await call.message.delete()
        keyboard = await all_memes_keyboard(meme_now=meme_now)
        await call.message.answer_photo(
            photo=all_memes[meme_now].photo_id,
            reply_markup=keyboard

        )

    else:
        msg = await call.answer("Это всё!")
"""
"""
@dp.callback_query_handler(Text(startswith='show_previous_global_meme'))
async def show_next_user_memes(call: types.CallbackQuery):
    all_memes = await get_all_memes()
    meme_now = int(call.data.split('_')[4])
    if meme_now < 0:
        meme_now = 0
    await call.message.delete()
    keyboard = await all_memes_keyboard(meme_now=meme_now)
    await call.message.answer_photo(
        photo=all_memes[meme_now].photo_id,
        # caption=f"",
        reply_markup=keyboard
    )
"""
"""
    for i in all_memes:
        await call.message.answer_photo(photo=i.photo_id)
"""
