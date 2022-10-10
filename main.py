#импортирование необходимых модулей библиотеки
from email import message
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import executor
import os
import emoji


from config import API_TOKEN      #импортировал константу

logging.basicConfig(level=logging.INFO)

bot= Bot(token=API_TOKEN)   #инициализация бота
dp = Dispatcher(bot)        #инициализация диспетчера


one = KeyboardButton('/1')
two = KeyboardButton('/2')
three = KeyboardButton('/3')
button_yes = KeyboardButton('/Да')
button_no = KeyboardButton('/Нет')
button_go = KeyboardButton('/Продолжить')
button_end = KeyboardButton('/Закончить')

result_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
hello_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
numbers_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

result_client.add(button_yes).add(button_no)
kb_client.row(button_yes, button_no).add(button_end)
hello_client.add(button_go)
numbers_client.add(one).add(two).add(three)



@dp.message_handler(commands=['start', 'help'])          #команды с которой начинается общение с ботом.
async def send_welcome(message: types.Message):          #асинхронная
    await message.reply('Привет!\nЯ "ЭхоБот".\nЯ работаю на "aiogram"\nМой создатель "Д Ш"\n@shooinj', reply_markup=hello_client)          #reply ссылается на сообщение пользователя

@dp.message_handler(commands=['Продолжить'])
async def start_command(message: types.Message):
    await message.answer('Добро пожаловать, в случайный генератор паролей.\nЗдесь вы можете создать случайный пароль, соответсвующий вашим критериям.\nХотите продолжить?', reply_markup=kb_client)

@dp.message_handler(commands=['Да'])
async def giving_inputs(message: types.Message):
    await message.reply('Сколько паролей вам нужно?', reply_markup=numbers_client)
@dp.message_handler(commands=['1'])
async def giving_inputs(message: types.Message):
    await message.reply('Длина одного пароля должна быть ...', reply_markup=numbers_client)

@dp.message_handler(commands=['Закончить'])
async def end_bot(message: types.Message):
    await message.reply('Увидимся позже.\nТы всегда можешь снова запустить меня, написав команду /start')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)      #запуск бота, пропускает обновления