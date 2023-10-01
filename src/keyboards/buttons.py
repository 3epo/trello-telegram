from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

""""Remove Button"""
removebtn = markup = ReplyKeyboardRemove()

""""Back button"""
backbtn = KeyboardButton("⬅️ Назад")

""""Cancel button"""
cancelbtn = KeyboardButton("❌ Отменить")
cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(cancelbtn)


""" Main Menu """
create_tiket = KeyboardButton("✅ Создать заявку")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(create_tiket)

""" Settings """
change_name = KeyboardButton("👤 Сменить имя")
change_number = KeyboardButton("📱 Сменить номер телефона")
settings = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(change_name,change_number).row(backbtn)

""" Change phone number """
send_number = KeyboardButton("📲 Отправить свой контакт",request_contact=True)
btn_send_number = ReplyKeyboardMarkup(resize_keyboard=True).row(send_number)

"""Tiket Accept"""
inline_get_tiket = InlineKeyboardButton('Приступить к заявке', callback_data='button1')
inline_tiket = InlineKeyboardMarkup().add(inline_get_tiket)

"""Tiket Close"""
inline_close_tiket = InlineKeyboardButton('⭐ Закрыть заявку', callback_data='button2')
inline_tiket_close = InlineKeyboardMarkup().add(inline_close_tiket)

"""Tiket Price"""
inline_payme = InlineKeyboardButton('Payme', url='https://payme.uz/5c0b6e6f002c486caedef72e')
inline_click = InlineKeyboardButton('Click', url='https://my.click.uz/clickp2p/2B9311472A27159BFDEDB1C9919914BFE71DEB09610136E3E65BFE17737BD201')
inline_apelsin = InlineKeyboardButton('Apelsin', url='https://www.apelsin.uz/express?code=ztUyaFakbP')
inline_payment = InlineKeyboardMarkup().add(inline_payme).add(inline_click).add(inline_apelsin)