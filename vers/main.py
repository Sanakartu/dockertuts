import telebot


bot = telebot.TeleBot("8262143266:AAEI4561c31tRdW60GPj6GVAHmtrmd4PJzI")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствую тебя в боте для проверки версий! Введи команду /help для получения информации о командах бота.")
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Пойди нахуй, я не хочу тебе помогать")


bot.polling(none_stop=True)