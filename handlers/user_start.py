from loader import dp, db
from aiogram import types


@dp.message_handler(commands='start')
async def user_start(message: types.Message):
    text = "Hi, Welcome"
    await message.answer(text=text)