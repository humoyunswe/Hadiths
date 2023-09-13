from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

info = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Sahih al Bukhari'),
            KeyboardButton('Sunan ibn Majah'),
        ],
        [
            KeyboardButton('Sunan Abu Dawud'),
            KeyboardButton('Muwatta Malik'),
        ],
        [
            KeyboardButton('Sahih Muslim'),
            KeyboardButton('Sunan an Nasai'),
        ],
        [
            KeyboardButton('Jami At Tirmidhi'),
        ],
    ]
)