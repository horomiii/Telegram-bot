
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command


TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig( 
level=logging.INFO, 
filename="bot.log", 
filemode="a", 
format="%(asctime)s - %(levelname)s - %(message)s" 
)


@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)
    

@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    new = { "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ё": "E", "Ж": "ZH",
            "З": "Z", "И": "I", "Й": "I", "К": "K", "Л": "L", "М": "M", "Н": "N", "О": "O",
            "П": "P", "Р": "R", "С": "S", "Т": "T", "У": "U", "Ф": "F", "Х": "KH", "Ц": "TS",
            "Ч": "CH", "Ш": "SH", "Щ": "SHCH", "Ы": "Y", "Ъ": "IE", "Э": "E", "Ю": "IU", "Я": "IA",
            
            "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh",
            "з": "z", "и": "i", "й": "i", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o",
            "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh", "ц": "ts",
            "ч": "ch", "ш": "sh", "щ": "shch", "ы": "y", "ъ": "ie", "э": "e", "ю": "iu", "я": "ia"}
    text = "".join(new.get(i,i) for i in text)
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(text=text)


if __name__ == '__main__':
    dp.run_polling(bot)
