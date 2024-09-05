from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command
from aiogram import F

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = Bot(token='7254708854:AAEop3TvQaazXTo8ZWx7djq8jBy1PMo4w-')
dp = Dispatcher()

# Функция обработки команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    # URL на ваше веб-приложение
    web_app_url = "https://your-github-pages-url.com"

    # Создание кнопки для Web App
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Open Web App", web_app=WebAppInfo(url=web_app_url))]
    ])

    # Отправка сообщения с кнопкой
    await message.answer("Нажмите на кнопку ниже, чтобы открыть веб-приложение:", reply_markup=keyboard)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
