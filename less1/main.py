import asyncio
import logging
import config
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логгирование
logging.basicConfig(level=logging.INFO)

# Создаем объект бота
bot = Bot(token=config.token)

# Диспечер
dp = Dispatcher()

# @dp.message(Command('start'))
# async def cmd_start(message: types.Message):
#     name = message.chat.first_name
#     print(message)
#     await message.answer(f'Hello, {name}')

@dp.message(Command('user'))
async def cmd_user(message: types.Message):
    user = message.from_user.first_name + ' ' + (message.from_user.last_name if message.from_user.last_name != None else "Без фамилии")
    await message.answer(f'Вас зовут: {user}')

@dp.message(Command('info'))
async def cmd_info(message: types.Message):
    info = "Этот бот был создан с целью прохождения курса Нейрохищник от GeekBrains"
    await message.answer(info)
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())