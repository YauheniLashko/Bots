import json
import logging
import token1

from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import bold

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ParseMode

from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

class StateMachine(StatesGroup):
    first_state = State()

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=token1.mazakafka)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['reg', 'start'])
async def reg(message: types.Message):
    kb = ReplyKeyboardMarkup(row_width=1)
    button = types.KeyboardButton("Сделай что-нибудь!")
    kb.add(button)
    telegram_id = message.from_user.id
    await message.answer("О, привет!", reply_markup=kb)

executor.start_polling(dp)
