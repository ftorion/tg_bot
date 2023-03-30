from  aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from base.base_bd import sql_add_command


class FSMadd(StatesGroup):
    name = State()
    description = State()
    price = State()

async def cm_srt(call):
    if call.data == "new":
        await FSMadd.name.set()
        await call.message.bot.send_message(call.message.chat.id, "name of the new service")

async def cm_start(msg: types.Message):
    if msg.text == "/new":
        await FSMadd.name.set()
        await msg.reply("name of the new service")


async def load_name(msg: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
        await FSMadd.next()
        await msg.reply("Enter a description")


async def load_description(msg: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['description'] = msg.text
        await FSMadd.next()
        await msg.reply("Enter a price")


async def load_price(msg: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['price'] = float(msg.text)

    await sql_add_command(state)
    await state.finish()

#доделать
async def com_cancellation(msg: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.reply("canceling the addition of a service")

def reg_ris(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands="new", state=None)
    dp.register_message_handler(load_name, state=FSMadd.name)
    dp.register_message_handler(load_description, state=FSMadd.description)
    dp.register_message_handler(load_price, state=FSMadd.price)
    dp.register_message_handler(com_cancellation, state="*", commands="cancellation")
    dp.register_message_handler(com_cancellation, Text(equals="cancellation", ignore_case=True), state="*")