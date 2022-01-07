from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

#   Import выше

#   Инициализация бота со значением token из другого файла
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)    #   Созданние диспетчера для бота

#   Обработчик команды start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, друг!\nЭто тестовая версия погодного бота)")

#   Обработчик команды help
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply('''
Функционал данного бота:
Просмотр прогноза погоды(t, влажность и тд.)
Автор: @pit_with_pizza
                        ''')

#   Обработчик любого сообщения, по сути он просто отправит то же самое что и получит
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

#   Эта часть кода отвечает за бесконечную проверку входящих сообщений
if __name__ == '__main__':
    executor.start_polling(dp)
