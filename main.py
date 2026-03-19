import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton
from aiogram.filters import CommandStart, Command
import os
from dotenv import load_dotenv
load_dotenv()

klaviatura = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Telefon3'), KeyboardButton(text='kanal3')],
        [KeyboardButton(text='Telefon4'), KeyboardButton(text='kanal4')],
    ],
resize_keyboard=True
)
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(msg:Message):
    await msg.answer("Salem adamlar")
@dp.message(Command('help'))
async def help(msg:Message):
    await msg.answer('ne jardem kerek')
@dp.message(Command('about'))
async def about(msg:Message):
    await msg.answer('telegram admin')
@dp.message(Command('baylanis'))
async def baylanis(msg:Message):
    await msg.answer('baylanis ushin nomer')
@dp.message(Command('telegram kanal'))
async def telegramkanallar(msg:Message):
    await msg.answer('kanallar')
@dp.message(Command('instagram'))
async def instagram(msg:Message):
    await msg.answer('insta tarmaq')

async def main():
    print('bot isledi')
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
