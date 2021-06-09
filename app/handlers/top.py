from re import sub

from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import quote_html, hbold

from app.functions.functions import split_list
from app.misc import dp
from app.models.Musics import Get_count


@dp.message_handler(commands=['top'])
async def top(message: Message):
    now_page = 1
    search_music = Get_count(now_page)
    if len(search_music) > 0:
        result_count = int(Get_count())
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
            keyboard_markup.insert(InlineKeyboardButton('➡', callback_data='top_next2'))
        await message.reply(send_text, reply_markup=keyboard_markup)
    else:
        await message.reply("Afsuski musiqa topilmadi!")
