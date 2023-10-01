from aiogram import Bot
from aiogram.types import Message

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'<b>Приветствую {message.from_user.first_name}. Рад тебя видеть!</b>')
    await message.answer(f'<s>Приветствую {message.from_user.first_name}. Рад тебя видеть!</s>')
    await message.reply(f'<tg-spoiler>Приветствую {message.from_user.first_name}. Рад тебя видеть!</tg-spoiler>')
