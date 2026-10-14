from config import BOT_TOKEN
from telegram import Bot
import asyncio

async def main():
    bot = Bot(token=BOT_TOKEN)

    me = await bot.get_me()
    print("اتصال موفق!")
    print("نام ربات:", me.first_name)
    print("نام کاربری:", me.username)

asyncio.run(main())