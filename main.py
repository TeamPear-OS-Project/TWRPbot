from botcommands import *
from telebot import util

@bot.message_handler(commands=['start', 'twrp', 'pbrp', 'ofox'])
def command_handler(m):
    command(m)

telebot.apihelper.RETRY_ON_ERROR = True

bot.infinity_polling()
