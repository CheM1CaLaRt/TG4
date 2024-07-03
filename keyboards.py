from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет! :)"), KeyboardButton(text="Пока! :(")]
], resize_keyboard=True)

inline_keyboard_links = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url="https://news.yandex.ru")],
   [InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru")],
   [InlineKeyboardButton(text="Видео", url="https://youtube.com")]
])


inline_keyboard_more = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше!", callback_data='more')]
])

options = ["Опция 1", "Опция 2"]

async def more_keyboard():
   keyboard = InlineKeyboardBuilder()
   for option in options:
       keyboard.add(InlineKeyboardButton(text=option, callback_data=option))
   return keyboard.adjust(2).as_markup()
