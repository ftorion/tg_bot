from aiogram import executor
import config
from config import  dp
from services import client, admin
admin.reg_ris(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=config.main_bot())

