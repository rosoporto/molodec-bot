import os
from telebot import TeleBot, types
from utils.handler_json import HandlerJson
from dotenv import load_dotenv
from  utils.get_logger import logger as log


load_dotenv(override=True)
tg_token = os.getenv("TG_TOKEN")
bot = TeleBot(tg_token)

handler_json = HandlerJson()


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    log.info(f"Пользователь {message.from_user.username} вызвал /start")
    bot.reply_to(message, "Привет! 👋 Я бот 'МОЛОДЕЦ'. Добавь привычку с /new_habit!")


# Обработчик команды /new_habit
@bot.message_handler(commands=['new_habit'])
def new_habit(message: types.Message):
    log.info(f"Пользователь {message.chat.id} вызвал /new_habit")
    bot.reply_to(message, "Напиши свою привычку!👇")
    bot.register_next_step_handler(message, save_habit)


def save_habit(message: types.Message):
    user_id = str(message.chat.id)
    habit = message.text.strip()
    if not habit:
        log.warning(f"Пользователь {user_id} ввёл пустую привычку")
        bot.reply_to(message, "Привычка не может быть пустой! Попробуй ещё раз с /new_habit")
        return

    data = handler_json.load_data
    data[user_id] = {
        "habit": habit,
        "progress": "",
        "day": 0,
        "last_date": ""
    }
    handler_json.load_data = data
    log.info(f"Пользователь {user_id} добавил привычку: {habit}")
    bot.reply_to(message, f"Привычка '{habit}' принята! Начни с /done, когда сделаешь первый шаг!")


if __name__ == "__main__":
    log.info("Bot starting!")
    bot.infinity_polling(skip_pending=True)
