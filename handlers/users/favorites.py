from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.favorites_keyboard import my_favorites_keyboard
from keyboards.inline.menu import menu
from loader import dp
from utils.db_api.db_commands import get_all_memes, create_row_favorites, get_user_favorites, delete_user_favorite


@dp.callback_query_handler(Text(startswith='add_to_favorites'))
async def adding_to_favorites(call: types.CallbackQuery):
    all_memes = await get_all_memes()
    meme = all_memes[int(call.data.split("_")[3])].photo_id
    favorite_memes = await get_user_favorites(call.from_user.id)

    if meme not in favorite_memes:
        await create_row_favorites(telegram_id=call.from_user.id, photo_id=meme)

        await call.answer("Мем успешно добавлен в избранное!")

    else:
        await call.answer("Этот мем уже есть в избранных!")


@dp.callback_query_handler(Text(equals='surfing_favorites'))
async def favorites_surf(call: types.CallbackQuery):
    data = await get_user_favorites(telegram_id=call.from_user.id)
    if len(data) > 0:
        await call.message.delete()
        keyboard = await my_favorites_keyboard(meme_now=0)
        await call.message.answer_photo(
            photo=data[0].photo_id,
            caption=f"Избранное\n"
                    f"Слот {str(1)}/{len(data)}",
            reply_markup=keyboard
        )

    else:
        await call.answer("Добавьте сначала что нибудь в избранное!")


@dp.callback_query_handler(Text(startswith='show_next_favorite'))
async def show_next_user_memes(call: types.CallbackQuery):
    data = await get_user_favorites(telegram_id=call.from_user.id)
    meme_now = int(call.data.split('_')[3])

    if len(data) > meme_now:
        keyboard = await my_favorites_keyboard(meme_now=meme_now)
        await call.message.delete()

        await call.message.answer_photo(
            photo=data[meme_now].photo_id,
            caption=f"Избранное\n"
                    f"Слот {meme_now+1}/{len(data)}",
            reply_markup=keyboard
        )

    else:
        msg = await call.answer("Это всё!")


@dp.callback_query_handler(Text(startswith='show_previous_favorite'))
async def show_next_user_memes(call: types.CallbackQuery):
    data = await get_user_favorites(telegram_id=call.from_user.id)
    meme_now = int(call.data.split('_')[3])
    if meme_now < 0:
        meme_now = 0
    await call.message.delete()
    keyboard = await my_favorites_keyboard(meme_now=meme_now)
    await call.message.answer_photo(
        photo=data[meme_now].photo_id,
        caption=f"Избранное\n"
                f"Слот {meme_now+1}/{len(data)}",
        reply_markup=keyboard
    )


@dp.callback_query_handler(Text(startswith='delete_favorite'))
async def delete_user_memes(call: types.CallbackQuery):
    data = await get_user_favorites(telegram_id=call.from_user.id)
    meme_now = int(call.data.split('_')[2])

    await delete_user_favorite(data[meme_now].photo_id)

    await call.answer("Мем удалён из избранного!")

    await call.message.delete()

    await call.message.answer(text="Менюшка:", reply_markup=menu)
