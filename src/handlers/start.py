from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from src.firebase import firebase
import re

from src.filters.is_private import IsPrivateFilter
import src.keyboards.buttons as kb

start_router = Router()
start_router.message.filter(IsPrivateFilter())

class Registration(StatesGroup):
    name = State()
    phone_number = State()
    org_name = State()

@start_router.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    if (firebase.regCheck(message.from_user.id)):
        await message.answer(f"Здравствуйте! Мы рады снова вас видеть ☺️",reply_markup=kb.mainMenu)#если запись имеется
        await state.clear()
    else:
        await message.answer(f'Здравствуйте! Вас приветсвует виртуальный менеджер Орлова Андрея. Как мне к вам обращаться?',reply_markup=kb.removebtn)
        await state.set_state(Registration.name)

@start_router.message(Registration.name)
async def start_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.phone_number)
    await message.answer(f"Очень приятно! Я буду вас звать {message.text}")
    await message.answer('Отправьте ваш номер телефона для связи с вами.',reply_markup=kb.btn_send_number)

@start_router.message(Registration.phone_number)
async def start_handler(message: types.Message, state: FSMContext):
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

    await state.update_data(phone_number=phone_number)
    await state.set_state(Registration.org_name)
    await message.answer(f"Ваш номер: {phone_number}",reply_markup=kb.removebtn)
    await message.answer('А теперь напишите название организации!')

@start_router.message(Registration.org_name)
async def start_handler(message: types.Message, state: FSMContext):
    await state.update_data(org_name=message.text)
    data = await state.get_data()
    await message.answer(f"Записали вашу организацию как: {message.text}!")
    firebase.createUser(message.from_user.id,message.from_user.first_name,message.from_user.last_name,message.from_user.username,data['name'],data['phone_number'],message.text)#создание записи
    await message.answer("✅ Спасибо за регистрацию!",reply_markup=kb.mainMenu)
    await state.clear()
