import telebot
TOKEN = '929241007:AAFrhbemrhXy-N8IVA0e0qy6dCMLYxHkj0Q'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


bot.polling()