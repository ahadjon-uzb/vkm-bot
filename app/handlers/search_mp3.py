from re import sub

from aiogram.types import ContentTypes, Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import quote_html, hbold

from app.functions.functions import split_list
from app.functions.keyboards import music_keyboard
from app.misc import dp
from app.models.Musics import Musics, Get_Music, Update_Count


@dp.message_handler(content_types=ContentTypes.TEXT)
async def _search_music(message: Message):
    music = Musics(message.text.lower())
    now_page = 1
    search_music = music.Search_Music(now_page)
    if len(search_music) > 0:
        result_count = int(music.All_Music())
        now_pages = int(now_page) * 10 if int(now_page) * 10 < result_count else result_count
        show_count_mp3 = int(now_page) * 10 - 9
        send_text = f"<b>Natijalar {show_count_mp3}-{now_pages} {result_count} dan\n\n</b>"
        keyboard_markup = InlineKeyboardMarkup()
        row_btns = []
        n = 1

        for music_ in search_music:
            row_btns.append(
                InlineKeyboardButton(f"{n}", callback_data=f"music{music_.id}")
            )
            title = sub('(\(@[A-Z_a-z0-9]+\))|(@[A-Z_a-z0-9]+)', '', music_.title)
            send_text += f"{hbold(n)}. {quote_html(title)}\n"
            n += 1
        for i in list(split_list(row_btns)):
            keyboard_markup.row(*i)

        keyboard_markup.row(InlineKeyboardButton('❌', callback_data='delete'))
        if result_count > 10:
            keyboard_markup.insert(InlineKeyboardButton('➡', callback_data='next2'))
        await message.reply(send_text, reply_markup=keyboard_markup)
    else:
        await message.reply("Hech narsa topilmadi 😔")


@dp.callback_query_handler(text_startswith=['music'])
async def get_music(query: CallbackQuery):
    username = (await dp.bot.get_me()).username
    music_id = query.data.replace('music', '')
    music = Get_Music(music_id)[0].file_id
    Update_Count(music_id)
    await query.message.reply_audio(music, reply_markup=music_keyboard(music_id),
                                    caption=f"🔥 @{username.capitalize()}")
