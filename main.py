import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery, ReplyKeyboardRemove

from config import TOKEN
import keyboards as kb


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer("Выберите действие:", reply_markup=kb.main)

@dp.message(F.text == "Привет! :)")
async def hi(message: Message):
   await message.answer(f"Привет {message.from_user.first_name}!", reply_markup= ReplyKeyboardRemove())

@dp.message(F.text == "Пока! :(")
async def bye(message: Message):
   await message.answer(f"До новых встреч {message.from_user.first_name}!", reply_markup= ReplyKeyboardRemove())

@dp.message(Command('links'))
async def links(message: Message):
   await message.answer("Ссылки:", reply_markup= kb.inline_keyboard_links)

@dp.message(Command('dynamic'))
async def links(message: Message):
   await message.answer("Динамические ссылки", reply_markup= kb.inline_keyboard_more)


@dp.callback_query(F.data == 'more')
async def more(callback: CallbackQuery):
   await callback.answer("Загружаю", show_alert=True)
   await callback.message.edit_text('Вот еще:', reply_markup=await kb.more_keyboard())

@dp.callback_query(F.data == 'Опция 1')
async def option1(message: Message):
   await message.answer("Опция 1")

@dp.callback_query(F.data == 'Опция 2')
async def option2(message: Message):
   await message.answer("Опция 2")



async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())