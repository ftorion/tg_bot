from aiogram import Bot, Dispatcher
from base import base_bd
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token="5956231422:AAHIlIjvF1YBxNdKDoWZf-tuhH_xUnxTyqg")
storage=MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def main_bot():
    print("bot start")
    base_bd.start_base()