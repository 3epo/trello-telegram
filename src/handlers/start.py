from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command

from src.filters.is_private import IsPrivateFilter

start_router = Router()
start_router.message.filter(IsPrivateFilter())

class Registration(StatesGroup):
    name = State()
    phone_number = State()
    org_name = State()

@start_router.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer(f"Здравствуйте! Вас приветсвует виртуальный менеджер Орлова Андрея. Как мне к вам обращаться?")

@start_router.message(Registration.name)
async def start_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.phone_number)
    await message.answer(f"Очень приятно! Я буду вас звать {message.text}")
    await message.answer('Отправьте ваш номер телефона для связи с вами.')

@start_router.message(Registration.phone_number)
async def start_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(Registration.org_name)
    await message.answer(f"Ваш номер +{message.text}")
    await message.answer('А теперь напишите название организации!')

@start_router.message(Registration.org_name)
async def start_handler(message: types.Message, state: FSMContext):
    await state.update_data(org_name=message.text)
    data = await state.get_data()
    await message.answer(f"Записали вашу организацию как: {message.text}!")
    await message.answer(f'Введенные данные:\nИмя:{data["name"]}\nНомер телефона:+{data["phone_number"]}\nОрганизация:{data["org_name"]}')
    await message.answer("✅ Спасибо за регистрацию!")
    await state.clear()



@start_router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")