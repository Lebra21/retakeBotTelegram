import telebot
TOKEN = '929241007:AAFrhbemrhXy-N8IVA0e0qy6dCMLYxHkj0Q'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def send_helper(message):
	bot.reply_to(message,"Darkhan idi nahui")

bot.polling()
