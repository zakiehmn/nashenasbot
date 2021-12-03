import telebot
from telebot import types
import random

unknown_messagesText=[]
sendBtnText = 'پیام ناشناس بفرست'
recieveBtnText = 'پیام ناشناس بگیر'
bot = telebot.TeleBot("2133638132:AAFVA1t7MZiQk1fNefh5gLO4TXVk0jiNCMk", parse_mode=None)
@bot.message_handler(commands=["start"])
def show_menu(message):
    markup = types.ReplyKeyboardMarkup()
    sendBtn = types.KeyboardButton(sendBtnText)
    recieveBtn = types.KeyboardButton(recieveBtnText)
    markup.row(sendBtn,recieveBtn)
    bot.send_message(message.chat.id, "انتخاب کنید:", reply_markup=markup)
    print(message)
    print(message.text)

@bot.message_handler(func = lambda message : message.text == sendBtnText)
def send_unknown_messsage(message):
    bot.send_message(message.chat.id, "پیام خود را بفرستید")
    @bot.message_handler(content_types=['text'])
    def get_sender_message(message):
        unknown_messagesText.append(message.text)
        for messageText in unknown_messagesText:
            print(messageText)
        bot.send_message(message.chat.id, "پیام شما به صورت ناشناس فرستاده میشود")


@bot.message_handler(func = lambda message : message.text == recieveBtnText)
def recieve_unknown_message(message):
    print(len(unknown_messagesText))
    if(len(unknown_messagesText)==0):
        bot.send_message(message.chat.id, "پیام ناشناسی موجود نیست")
    else:
        unknownMessage = random.choice(unknown_messagesText)
        bot.send_message(message.chat.id, unknownMessage)
        unknown_messagesText.remove(unknownMessage)    


bot.infinity_polling()