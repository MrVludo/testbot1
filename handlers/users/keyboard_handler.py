from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import message

from keyboards.inline.settings1 import settings1, settings_keyboard
from loader import dp

from keyboards.inline.menu import menu
from keyboards.inline.returnto_infopanel_kb import returnto_infopanel
from keyboards.inline.user_info_menu import user_info_menu
from states.get_info import GetInfo
from utils.db_api.db_commands import select_user, update_settings, update_nickname, update_description
from keyboards.inline.info_panel import info_panel


@dp.callback_query_handler(Text(equals='returntomenu'))
async def start_menu(call: types.CallbackQuery):
    await call.message.edit_text('Менюшка', reply_markup=menu)


# Замена никнейма:

@dp.callback_query_handler(Text(equals='change_name'))
async def name_changing(call: types.CallbackQuery):
    msg = await call.message.edit_text("Придумайте новое имя!", reply_markup=returnto_infopanel)
    await GetInfo.name.set()

    state = dp.current_state(user=call.from_user.id)

    await state.update_data(
        {
            'message_id': msg.message_id
        }
    )


@dp.message_handler(state=GetInfo.name)
async def get_name_from_user(message: types.Message, state: FSMContext):
    name = message.text
    await message.delete()

    await update_nickname(
        telegram_id=message.from_user.id,
        nickname=name
    )

    data = await state.get_data()
    message_id = data.get('message_id')

    user = await select_user(telegram_id=message.from_user.id)
    await dp.bot.edit_message_text(
        chat_id=message.from_user.id,
        message_id=message_id,
        text=f'Ваш никнейм: {"Отсутствует" if user.nickname is None else user.nickname}\n'
             f'Ваше описание: {"Отсутствует" if user.description is None else user.description}',
        reply_markup=user_info_menu
    )

    await state.reset_state(True)


# Замена описания:

@dp.callback_query_handler(Text(equals='change_description'))
async def name_changing(call: types.CallbackQuery):
    msg = await call.message.edit_text("Придумайте новое описание!", reply_markup=returnto_infopanel)
    await GetInfo.description.set()

    state = dp.current_state(user=call.from_user.id)

    await state.update_data(
        {
            'message_id': msg.message_id
        }
    )


@dp.message_handler(state=GetInfo.description)
async def get_name_from_user(message: types.Message, state: FSMContext):
    description = message.text
    await message.delete()

    await update_description(
        telegram_id=message.from_user.id,
        description=description
    )

    data = await state.get_data()
    message_id = data.get('message_id')

    user = await select_user(telegram_id=message.from_user.id)
    await dp.bot.edit_message_text(
        chat_id=message.from_user.id,
        message_id=message_id,
        text=f'Ваш никнейм: {"Отсутствует" if user.nickname is None else user.nickname}\n'
             f'Ваше описание: {"Отсутствует" if user.description is None else user.description}',
        reply_markup=user_info_menu
    )

    await state.reset_state(True)


# Замена настроек:

@dp.callback_query_handler(Text(equals="show_settings"))
async def settings(call: types.CallbackQuery):
    user = await select_user(telegram_id=call.from_user.id)
    keyboard = await settings_keyboard(status=user.settings)
    await call.message.edit_text(f'Показывать ли ваши мемы другим?\n'
                                 f'Статус: {"Да" if user.settings else "Нет"}', reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='settings_to'))
async def change_settings_true(call: types.CallbackQuery):
    data = call.data.split('_')

    await update_settings(
        telegram_id=call.from_user.id,
        setting=data[2]
    )

    await call.answer(f'Вы успешно изменили ваш статус на: {"Да" if data[2] == "True" else "Нет"}')

    user = await select_user(telegram_id=call.from_user.id)
    keyboard = await settings_keyboard(status=user.settings)
    await call.message.edit_text(f'Показывать ли ваши мемы другим?\n'
                                 f'Статус: {"Да" if user.settings else "Нет"}', reply_markup=keyboard)


# Панельки:

@dp.callback_query_handler(Text(equals='returnto_infomenu'))
async def start_menu(call: types.CallbackQuery):
    user = await select_user(telegram_id=call.from_user.id)
    await call.message.edit_text(f'Ваш никнейм: {"Отсутствует" if user.nickname is None else user.nickname}\n'
                                 f'Ваше описание: {"Отсутствует" if user.description is None else user.description}',
                                 reply_markup=user_info_menu)


@dp.callback_query_handler(Text(equals='show_info'))
async def start_menu(call: types.CallbackQuery):
    user = await select_user(telegram_id=call.from_user.id)
    await call.message.edit_text(f'Ваш никнейм: {"Отсутствует" if user.nickname is None else user.nickname}\n'
                                 f'Ваше описание: {"Отсутствует" if user.description is None else user.description}',
                                 reply_markup=user_info_menu)


@dp.callback_query_handler(Text(equals="show_info_panel"), state='*')
async def start_panel(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(True)
    user = await select_user(telegram_id=call.from_user.id)
    await call.message.edit_text(f'Ваш никнейм: {"Отсутствует" if user.nickname is None else user.nickname}\n'
                                 f'Ваше описание: {"Отсутствует" if user.description is None else user.description}',
                                 reply_markup=info_panel)



