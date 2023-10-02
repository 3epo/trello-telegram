from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardRemove)

""""Remove Button"""
removebtn = ReplyKeyboardRemove()

""""Back button"""
backbtn = KeyboardButton(text='⬅️ Назад')

""""Cancel button"""
cancelbtn = KeyboardButton(text='❌ Отменить')
cancel = ReplyKeyboardMarkup(keyboard=[[cancelbtn]], resize_keyboard=True)

""" Main Menu """
create_tiket = KeyboardButton(text="✅ Создать заявку")
mainMenu = ReplyKeyboardMarkup(keyboard=[[create_tiket]],resize_keyboard=True)

""" Settings """
settingsbtn = [
    KeyboardButton(text="👤 Сменить имя"),
    KeyboardButton(text="📱 Сменить номер телефона")
]

settings = ReplyKeyboardMarkup(keyboard=[settingsbtn, [cancelbtn]], resize_keyboard=True, one_time_keyboard=True)

""" Change phone number """
send_number = KeyboardButton(text="📲 Отправить свой контакт",request_contact=True)
btn_send_number = ReplyKeyboardMarkup(keyboard=[[send_number]],resize_keyboard=True)

"""Tiket Accept"""
inline_tiket = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Приступить к заявке', callback_data='button1')]
    ]
)

"""Tiket Close"""
inline_tiket_close = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text='⭐ Закрыть заявку', callback_data='button2')]
    ]
)

"""Tiket Price"""
inline_payment = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Payme', url='https://payme.uz/5c0b6e6f002c486caedef72e')],
        [InlineKeyboardButton(text='Click', url='https://my.click.uz/clickp2p/2B9311472A27159BFDEDB1C9919914BFE71DEB09610136E3E65BFE17737BD201')],
        [InlineKeyboardButton(text='Apelsin', url='https://www.apelsin.uz/express?code=ztUyaFakbP')]
    ]
)
