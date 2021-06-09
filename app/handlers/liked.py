from app.models.Database import Playlist
from re import sub

from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold, quote_html

from app.functions.functions import Playlists, split_list
from app.misc import dp


@dp.callback_query_handler(text_startswith=['like'])
async def _playlist(query: CallbackQuery):
    data = query.data
    music_id = data.replace('like', '')
    added = Playlists(music_id=int(music_id), user_id=query.from_user.id).delete_or_add(
        title=f"{query.message.audio.performer} - {query.message.audio.title}", file_id=query.message.audio.file_id)
    if added:
        await query.answer("💔  Playlistdan o'chirildi")
    else:
        await query.answer("❤️ Sizning playlistingizga qo'shildi (/my)")


@dp.message_handler(commands=['my'])
async def _playlists(message: Message):
    now_page = 1

    _playlist = Playlists(message.from_user.id)
    playlist_count = _playlist.lists_count()
    if playlist_count > 0:
        playlist = _playlist.lists(now_page)
        send_text = ""
        keyboard_markup = InlineKeyboardMarkup()
        row_btns = []
        n = 1
        for music_ in playlist:
            row_btns.append(
                InlineKeyboardButton(
                    f"{n}", callback_data=f"music{music_.music_id}")
            )
            title = sub(
                '(\(@[A-Z_a-z0-9]+\))|(@[A-Z_a-z0-9]+)', '', music_.title)
            send_text += f"{hbold(n)}. {quote_html(title)}\n"
            n += 1
        for i in list(split_list(row_btns)):
            keyboard_markup.row(*i)

        keyboard_markup.row(InlineKeyboardButton('❌', callback_data='delete'))
        if playlist_count > 10:
            keyboard_markup.insert(
                InlineKeyboardButton('➡', callback_data='playlist_next2'))
        await message.reply(send_text, reply_markup=keyboard_markup)
    else:
        await message.reply("Hech narsa topilmadi 😔")
