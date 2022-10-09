from email import message
import logging


#This is my first echo bot written in aiogram 


from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5502461822:AAHk_yWHkTsqz3xyo5WgAELYOlgmESpO_78'

logging.basicConfig(level=logging.INFO)

bot= Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Привет!\nЯ "ЭхоБот".\nЯ работаю на "aiogram"\nМой создатель "Д Ш"')

@dp.message_handler(commands=['go'])
async def send_message(message: types.Message):
    await message.reply('Я буду повторять за тобой')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
