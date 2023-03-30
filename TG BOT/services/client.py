from config import bot, dp
from aiogram import types
import key
from base.base_bd import sql_read
from services.admin import cm_srt

@dp.message_handler(commands="start")
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, r"Hi, I'm a Bot for your haircut write a command /manu", reply_markup=key.gret_kb)

@dp.message_handler(commands="manu")
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id,"My command", reply_markup= types.ReplyKeyboardRemove())
    await bot.send_message(msg.from_user.id, f"Services - /serv \nRegistration for a haircut - /regis \nAddress - /address \nDiscounts - /discounts", reply_markup=key.inline_kb)


@dp.callback_query_handler()
async def vote_callback(call : types.CallbackQuery):
    if call.data == "address":
        await call.message.bot.send_location(call.message.chat.id, 10, 19, 10)
        await call.message.bot.send_message(call.message.chat.id, "We work around the clock")
    elif call.data == "discounts":
        await call.message.bot.send_photo(call.message.chat.id, photo="https://lagunahotel.ru/wp-content/uploads/2020/12/20.png")
        await call.message.bot.send_message(call.message.chat.id, "Discounts for pensioners, disabled people, children under 7 years old,"
                                                                  " students and pregnant women 20% discount from the total amount of services")
    elif call.data == "serv":
         await sql_read(call)
    elif call.data == "new":
        await cm_srt(call)







