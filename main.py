import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(msg:Message):
    await msg.answer("Salem adamlar")

async def main():
    print('bot isledi')
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
