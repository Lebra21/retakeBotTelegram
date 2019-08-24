import telebot , constants , random , os
from telebot.types import Message

bot = telebot.TeleBot(constants.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def send_helper(message):
	bot.reply_to(message,"Darkhan idi nahui")

# Обработчик для документов и аудиофайлов


 # Обработчик сообщений, содержащих документ с mime_type 'text/plain' (обычный текст)
@bot.message_handler(func=lambda message: True)
def send_smile(message: Message):
    bot.reply_to(message, random.choice(constants.SMILES))

bot.polling()
