from asyncio import sleep

from aiogram.types import ContentTypes, Message
from aiogram.utils.exceptions import RetryAfter

from app.misc import dp
from app.models.Musics import New_Music


@dp.message_handler(content_types=ContentTypes.AUDIO)
async def _(message: Message):
    music_data = f"{message.audio.performer} - {message.audio.title}"
    try:
        await message.reply(New_Music(music_data, message.audio.file_id))
    except RetryAfter as e:
        await sleep(e.timeout)
