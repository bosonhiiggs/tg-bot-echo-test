import telebot

bot = telebot.TeleBot('5494023430:AAHC7tphPbiS9gtVuMHao1r23SaRoliVWvE') # Создание экземпляра бота

@bot.message_handler(commands=["start"]) #Ответ на "start"
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я тут!')

@bot.message_handler(content_types=["text"]) # Ответ на полученное сообщение пользователя
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

bot.polling(none_stop=True)
