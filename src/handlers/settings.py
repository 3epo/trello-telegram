from aiogram import types, Router,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from src.firebase import firebase
import re

from src.filters.is_private import IsPrivateFilter
import src.keyboards.buttons as kb

settings_router = Router()
settings_router.message.filter(IsPrivateFilter())

class Settings(StatesGroup):
    change_phone = State()
    change_name = State()

'''' Главное меню настроек '''
@settings_router.message(Command('settings'))
async def settings_handler(message: types.Message):
    await message.answer(f"Пришло время перемен! Что будем менять?",reply_markup=kb.settings)

'''' Кнопка сменить номер телефона '''
@settings_router.message(F.text == "❌ Отменить")
async def settings_handler(message: types.Message):
    await message.answer(f"Мы вернулись! Создадим заявку?",reply_markup=kb.mainMenu)

'''' Кнопка сменить номер телефона '''
@settings_router.message(F.text == "📱 Сменить номер телефона")
async def change_phone(message: types.Message, state: FSMContext):
    await message.answer("Отправьте нам ваш контакт",reply_markup=kb.btn_send_number)
    await state.clear()
    await state.set_state(Settings.change_phone)

'''' Обработка отправленого контакта для изменения номера'''
@settings_router.message(Settings.change_phone)
async def get_phone(message: types.Message, state: FSMContext):
    if message.contact is not None:
        # Если пользователь поделился контактом
        phone_number = message.contact.phone_number
    else:
        # Если пользователь ввел номер вручную
        phone_number = message.text

        # Проверка на валидность номера телефона
        if not re.match(r"(\+998|998)[0-9]{9}$", phone_number):
            await message.answer("Пожалуйста, введите действительный номер телефона.")
            return
    firebase.updateUserPhone(phone_number,message.from_user.id)
    await state.clear()
    await message.answer("✅ Ваш номер успешно изменен.",reply_markup=kb.mainMenu)

@settings_router.message(F.text == "👤 Сменить имя")
async def change_name(message: types.Message, state: FSMContext):
    await message.answer("Как вас нам называть?")
    await state.clear()
    await state.set_state(Settings.change_name)

'''' Обработка отправленого контакта для изменения имени'''
@settings_router.message(Settings.change_name)
async def get_name(message: types.Message, state: FSMContext):
    username = message.text
    firebase.updateUserName(username,message.from_user.id)
    await state.clear()
    await message.answer(f"✅ Теперь мы будем вас называть {message.text}.",reply_markup=kb.mainMenu)