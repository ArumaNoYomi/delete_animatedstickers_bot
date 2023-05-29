from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentTypes
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=ContentTypes.all())
async def check(message: types.Message):
    if message.text:
        return
    if message.sticker.is_video or message.sticker.is_animated:
        await message.delete()

executor.start_polling(dp, skip_updates=True)