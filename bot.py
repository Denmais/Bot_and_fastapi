from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv
import os


async def send(msg):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    load_dotenv()
    txt = f'''{msg}'''

    session = AiohttpSession()
    bot = Bot(token=os.getenv('TOKEN'), session=session)
    await bot.send_message(chat_id=-1002439838642, text=txt)
    await bot.session.close()
