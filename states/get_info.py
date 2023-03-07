from aiogram.dispatcher.filters.state import StatesGroup, State


class GetInfo(StatesGroup):
    name = State()
    description = State()
    photo = State()
