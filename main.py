import os
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message
from dotenv import load_dotenv

# Tokenni yuklash .env fayldan
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN", "7349755281:AAFUvG5-nKmwGkyZA899y6YYWOudbUvPip4")

# Bot va Dispatcher obyektlarini yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Yangi foydalanuvchi qo‘shilganda xizmat xabarini o‘chirish
@dp.message(F.content_type == types.ContentType.NEW_CHAT_MEMBERS)
async def delete_new_member_message(message: Message):
    try:
        await bot.delete_message(message.chat.id, message.message_id)
        print("Yangi foydalanuvchi qo‘shilish xabari o‘chirildi.")
    except Exception as e:
        print(f"Xabarni o‘chirishda xatolik: {e}")

# Foydalanuvchi guruhdan chiqib ketganda xizmat xabarini o‘chirish
@dp.message(F.content_type == types.ContentType.LEFT_CHAT_MEMBER)
async def delete_left_member_message(message: Message):
    try:
        await bot.delete_message(message.chat.id, message.message_id)
        print("Foydalanuvchi chiqib ketish xabari o‘chirildi.")
    except Exception as e:
        print(f"Xabarni o‘chirishda xatolik: {e}")

# Asosiy ishga tushirish funksiyasi
async def main():
    print("Bot ishga tushmoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
