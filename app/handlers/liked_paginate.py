from re import sub

from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold, quote_html

from app.functions.functions import split_list, Playlists
from app.misc import dp


@dp.callback_query_handler(text_startswith=['playlist_next', 'playlist_prev'])
async def __search_music(query: CallbackQuery):
    now_page = query.data.replace('playlist_next', '') if query.data.startswith(
        'playlist_next') else query.data.replace('playlist_prev', '')
    prev_page = int(now_page) - 1
    next_page = int(now_page) + 1
    _playlist = Playlists(query.from_user.id)
    playlist_count = _playlist.lists_count()
    if playlist_count > 0:
        playlist = _playlist.lists(int(now_page))
        keyboard_markup = InlineKeyboardMarkup()
        n = 1
        row_btns = []
        send_text = ""
        for i in playlist:
            row_btns.append(
                InlineKeyboardButton(f"{n}", callback_data=f"music{i.id}")
            )
            title = sub('(\(@[A-Z_a-z0-9]+\))|(@[A-Z_a-z0-9]+)', '', i.title)

            send_text += f"{hbold(n)}. {quote_html(title)}\n"
            n += 1
        for i in list(split_list(row_btns)):
            keyboard_markup.row(*i)
        if prev_page != 0:
            keyboard_markup.row(InlineKeyboardButton(
                '⬅', callback_data=f'playlist_prev{prev_page}'))
        keyboard_markup.insert(
            InlineKeyboardButton('❌', callback_data='delete'))
        if 10 < playlist_count and playlist_count > int(now_page) * 10:
            keyboard_markup.insert(InlineKeyboardButton(
                '➡', callback_data=f'playlist_next{next_page}'))
        await query.message.edit_text(send_text,
                                      reply_markup=keyboard_markup)
    else:
        print(playlist_count)
