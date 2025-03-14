import os
import telebot
from dotenv import load_dotenv


load_dotenv(override=True)
tg_token = os.getenv("TG_TOKEN")
bot = telebot.TeleBot(tg_token)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! 👋 Я бот 'МОЛОДЕЦ'. Добавь привычку с /new_habit!")


if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)