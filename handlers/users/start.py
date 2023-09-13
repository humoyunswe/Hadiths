from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.imams import info
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}! I am a bot for getting hadith from Sahih al-Bukhari. Just send the command <b>/hadith</b> and I will send you a random hadith.",reply_markup=info)
