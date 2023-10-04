from aiogram import types, Router,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command

from src.filters.is_private import IsPrivateFilter
import src.keyboards.buttons as kb

settings_router = Router()
settings_router.message.filter(IsPrivateFilter())

class Settings(StatesGroup):
    change_phone = State()
    get_phone = State()

    change_name = State()
    get_name = State()

'''' Главное меню настроек '''
@settings_router.message(Command('settings'))
async def settings_handler(message: types.Message):
    await message.answer(f"Пришло время перемен! Что будем менять?",reply_markup=kb.settings)

'''' Кнопка сменить номер телефона '''
@settings_router.message(F.text == "👤 Сменить имя")
async def settings_handler(message: types.Message):
    await message.answer(f"иди на хуй!",reply_markup=kb.settings)