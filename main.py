import telebot , constants , random , os , time
from telebot.types import Message


bot = telebot.TeleBot(constants.TOKEN)
keyboard = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard.row('Alisher is monkey?','/help')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome!",reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def send_helper(message):
	bot.reply_to(message,"Darkhan idi nahui")

# Обработчик для документов и аудиофайлов


 # Обработчик сообщений, содержащих документ с mime_type 'text/plain' (обычный текст)
@bot.message_handler(func=lambda message: True)
def send_smile(message: Message):
    if 'Alisher is monkey?' in message.text:
        bot.reply_to(message, random.choice(constants.smiles))
        return
    else:
        pass


while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        time.sleep(15)