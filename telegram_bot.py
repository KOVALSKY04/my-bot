import random
import telebot
from telebot.types import Message

TOKEN = "946012931:AAHXidGnIa51MVNgpQ1Ho9CRbxfseK7D_gI"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_hendler(message: Message):
    bot.reply_to(message, 'There is no answer =(')


@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    if 'Alex Goodkid' in message.text:
        bot.reply_to(message, 'Alex is good kid')
        return

    bot.reply_to(message, str(random.random()))


bot.polling(timeout=60)
