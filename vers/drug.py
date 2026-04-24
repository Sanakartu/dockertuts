import telebot

bot = telebot.TeleBot("318698634:AAFb7Ouy9cMd1flNEtNxv9NXvw46NOFOUUk")

# Текст, который бот будет отвечать ВСЕГДА
ANSWER_TEXT = "Привет! Это автоответчик 😊"

@bot.message_handler(commands=['start'])
def auto_reply(message):
    bot.send_message(message.chat.id, ANSWER_TEXT)

print("Бот запущен...")
bot.polling(none_stop=True)c:\Users\sanak\Downloads\Telegram Desktop\Setup.sql.txt