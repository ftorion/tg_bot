from  aiogram.types import  ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
b1 = KeyboardButton("/manu")
gret_kb = ReplyKeyboardMarkup(resize_keyboard=True)
gret_kb.add(b1)



botton = [
     types.InlineKeyboardButton("/serv", callback_data="serv"),
     types.InlineKeyboardButton("/new", callback_data="new"),
     types.InlineKeyboardButton("/address", callback_data="address"),#1
     types.InlineKeyboardButton("/discounts", callback_data="discounts"),#1
]


inline_kb = InlineKeyboardMarkup(row_width=2)
inline_kb.add(*botton)
