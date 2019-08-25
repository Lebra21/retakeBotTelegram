import telebot , constants , random , os , time
from telebot.types import Message , ReplyKeyboardRemove


bot = telebot.TeleBot(constants.TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('/start','/stop')
    user_markup.row('photo','audio','media')
    user_markup.row('sticker','video','voice','location')
    bot.send_message(message.from_user.id,'Welcome!',reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def send_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id,'...',reply_markup=hide_markup)

@bot.message_handler(commands=['help'])
def send_helper(message):
	bot.reply_to(message,"Darkhan 0 help")

# Обработчик для документов и аудиофайлов

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'photo':
        directory = 'C:/Users/user/PycharmProjects/retakersBotTelegram/files/photos'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file,'rb')
        bot.send_chat_action(message.from_user.id,'upload_photo')
        bot.send_photo(message.from_user.id,img)
        img.close()
    elif message.text == 'voice':
        voice = open("C:/Users/user/PycharmProjects/retakersBotTelegram/files/voice/Папич-—-Здарова-_www.mixmuz.ru_.ogg",'rb')
        bot.send_chat_action(message.from_user.id, 'upload_voice')
        bot.send_voice(message.from_user.id, voice)
        voice.close()
    elif message.text == 'location':
        bot.send_chat_action(message.from_user.id,'upload location')
        bot.send_location(message.from_user.id,43.207836,76.669086)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        time.sleep(15)