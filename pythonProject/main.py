import telebot
import  logging
from telegram import Update
from telebot import types
from Qoshimcha import valyutalar, barchasi, usd ,rubl
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN =  "your token here"
valyuta = telebot.TeleBot(token=TOKEN)
america = "\U0001F1FA\U0001F1F8"
uzbekistan = "\U0001F1FA\U0001F1FF"
russia = "\U0001F1F7\U0001F1FA"

@valyuta.message_handler(commands=['start'])
def send(message):

    valyuta.reply_to(message, valyutalar())


@valyuta.message_handler(commands=["barcha_valyutalar"])
def all_currency(message):
    valyuta.reply_to(message,barchasi)
    print("Barcha valyutalar!")


@valyuta.message_handler(commands=['hisoblash'])
def hisoblash(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton(f"usd {america} > uzs {uzbekistan}", callback_data='usd')
    item2 = types.InlineKeyboardButton(f"rubl {russia} > uzs {uzbekistan}", callback_data='ruble')
    item3 = types.InlineKeyboardButton(f"uzs {uzbekistan} > usd {america}", callback_data='uzs')
    item4 = types.InlineKeyboardButton(f"uzs {uzbekistan} > rubl {russia}", callback_data='uzs_to_ruble')

    markup.add(item1, item2, item3, item4)
    valyuta.send_message(message.chat.id, "Qaysi valyutani hisoblamoqchisiz?:", reply_markup=markup)



@valyuta.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'usd':
        valyuta.send_message(call.message.chat.id, "USD ni kiriting \nfaqat raqam bilan yozing\ne.g: 100 ")
        @valyuta.message_handler(func=lambda message: True)
        def salom(message):
            text = float(message.text.lower())
            if text:
                text = str(text * usd)+" UZS"
                valyuta.reply_to(message,text)


    if call.data == 'ruble':
        valyuta.send_message(call.message.chat.id, "RUBLE ni kiriting \nfaqat raqam bilan yozing\ne.g: 100 ")
        @valyuta.message_handler(func=lambda message: True)
        def salom(message):
            text = float(message.text.lower())
            if text:
                text = str(text * rubl) + " UZS"
                valyuta.reply_to(message, text)


    if call.data == "uzs":
        valyuta.send_message(call.message.chat.id,"UZS ni kiriting \nfaqat raqam bilan yozing\ne.g: 100000 ")
        @valyuta.message_handler(func=lambda message: True)
        def salom(message):
            text = float(message.text.lower())
            if text:
                text = str(  text // usd) + " USD\nyaxlitlangan xolatda!"
                valyuta.reply_to(message, text)

    #

    if call.data == "uzs_to_ruble":
        valyuta.send_message(call.message.chat.id,"UZS ni kiriting \nfaqat raqam bilan yozing\ne.g: 100000 ")
        @valyuta.message_handler(func=lambda message: True)
        def salom(message):
            text = float(message.text.lower())
            if text:
                text = str(  text * rubl) + " USD\nyaxlitlangan xolatda!"
                valyuta.reply_to(message, text)




@valyuta.message_handler(content_types=['text'])
def foto(message):
    
    if message.text.lower() == "foto":
        with open("foto.jpg", "rb") as foto:
            valyuta.send_photo(message.chat.id, foto,caption="Beach",parse_mode="nothing")

    if message.text.lower() == "music":
        with open("music.mp3","rb") as music:
            valyuta.send_audio(message.chat.id,music,caption="Successfully",duration=4)


valyuta.polling()
