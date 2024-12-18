from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv
import os


async def send(msg):
    load_dotenv()
    txt = f'''{msg}'''

    session = AiohttpSession()
    bot = Bot(token=os.getenv('TOKEN'), session=session)
    await bot.send_message(chat_id=os.getenv('chat_id'), text=txt, parse_mode='HTML')
    await bot.session.close()
