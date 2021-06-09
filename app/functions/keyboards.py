from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def music_keyboard(music_id):
    keyboard_markup = InlineKeyboardMarkup()
    keyboard_markup.row(
        InlineKeyboardButton("❤️/💔", callback_data=f'like{music_id}'),
        InlineKeyboardButton("❌", callback_data='delete')
    )
    return keyboard_markup
