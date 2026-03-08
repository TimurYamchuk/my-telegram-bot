import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Вставь сюда свой токен от BotFather
TOKEN = "ТВОЙ_ТОКЕН_БОТА"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я запущен внутри Docker-контейнера через CI/CD!")

@dp.message()
async def echo_handler(message: types.Message):
    await message.send_copy(chat_id=message.chat.id)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())