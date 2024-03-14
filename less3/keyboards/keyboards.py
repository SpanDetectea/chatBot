from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/prof')
button4 = types.KeyboardButton(text='Покажи лису')
button5 = types.KeyboardButton(text='/male')

keyboard1 = [
[button1, button2],
[button4, button5],
]

keyboard2 = [
[button4],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)