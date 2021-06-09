from aiogram.types import ChatType, Message, CallbackQuery

from app.misc import dp
from app.models import Chats


@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['start'])
async def send_welcome(message: Message):
    Chats.User(message.from_user.id)
    text = """Shunchaki menga qo'shiqchi yoki qo'shiq nomini jo'nating va men siz uchun musiqa topib beraman!

/start - Botni qayta ishga tushirish
/top - Eng ko'p tinglangan musiqalar
/my - Sizning playlist
"""
    await message.reply(text,
                        disable_web_page_preview=True, parse_mode="Html")


@dp.callback_query_handler(text_startswith=['delete'])
async def _delete_message(query: CallbackQuery):
    await query.message.delete()
