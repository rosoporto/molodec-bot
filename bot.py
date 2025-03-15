import os
from telebot import TeleBot, types
from utils.handler_json import HandlerJson
from utils.messages import Messages
from dotenv import load_dotenv
from utils.get_logger import logger as log
import datetime


load_dotenv(override=True)
tg_token = os.getenv("TG_TOKEN")
bot = TeleBot(tg_token)

handler_json = HandlerJson()
data = handler_json.load_data
messages = Messages()


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    log.info(f"Пользователь {message.from_user.username} вызвал /start")
    bot.reply_to(message, messages.WELCOME, parse_mode="MarkdownV2")


# Обработчик команды /new_habit
@bot.message_handler(commands=['new_habit'])
def new_habit(message: types.Message):
    log.info(f"Пользователь {message.chat.id} вызвал /new_habit")
    bot.reply_to(message, messages.NEW_HABIT_PROMPT)


def save_habit(message: types.Message):
    user_id = str(message.chat.id)
    habit = message.text.strip()
    if not habit:
        log.warning(f"Пользователь {user_id} ввёл пустую привычку")
        bot.reply_to(message, messages.HABIT_EMPTY)
        return

    data[user_id] = {
        "habit": habit,
        "progress": "",
        "day": 0,
        "last_date": ""
    }
    handler_json.load_data = data
    log.info(f"Пользователь {user_id} добавил привычку: {habit}")
    bot.reply_to(message, messages.HABIT_ACCEPTED(habit))


# Обработчик команды /done
@bot.message_handler(commands=['done'])
def done(message: types.Message):
    user_id = str(message.chat.id)
    if user_id not in data:
        log.warning(f"Пользователь {user_id} вызвал /done без привычки")
        bot.reply_to(message, messages.NO_HABIT)
        return

    today = datetime.date.today().isoformat()
    last_date = data[user_id]["last_date"]

    # Начало цикла
    if data[user_id]["day"] == 0:
        data[user_id]["progress"] = "М"
        data[user_id]["day"] = 1
        data[user_id]["last_date"] = today
        log.info(f"Пользователь {user_id} начал привычку '{data[user_id]['habit']}'")
        bot.reply_to(message, messages.DONE_START(data[user_id]["habit"]))
    else:
        # Проверка пропуска
        if last_date:
            last = datetime.date.fromisoformat(last_date)
            diff = (datetime.date.fromisoformat(today) - last).days
            if diff > 1:
                data[user_id]["progress"] = ""
                data[user_id]["day"] = 0
                data[user_id]["last_date"] = today
                log.info(f"Пользователь {user_id} пропустил день, привычка '{data[user_id]['habit']}' сброшена")
                bot.reply_to(message, messages.DONE_MISSED(data[user_id]["habit"]))
                handler_json.load_data = data
                return

        # Прогресс
        data[user_id]["day"] += 1
        letters = "МОЛОДЕЦ"
        data[user_id]["progress"] = letters[:data[user_id]["day"]]
        data[user_id]["last_date"] = today

        if data[user_id]["day"] == 7:
            log.info(f"Пользователь {user_id} завершил привычку '{data[user_id]['habit']}'")
            bot.reply_to(message, messages.DONE_COMPLETE(data[user_id]["habit"]))
            data[user_id]["progress"] = ""
            data[user_id]["day"] = 0
        else:
            log.info(f"Пользователь {user_id} продвинулся: {data[user_id]['progress']} ({data[user_id]['day']}/7)")
            bot.reply_to(message, messages.DONE_PROGRESS(data[user_id]["habit"], data[user_id]["progress"], data[user_id]["day"]))

    handler_json.load_data = data


# Обработчик команды /skip
@bot.message_handler(commands=['skip'])
def skip(message: types.Message):
    user_id = str(message.chat.id)
    if user_id not in data:
        log.warning(f"Пользователь {user_id} вызвал /skip без привычки")
        bot.reply_to(message, messages.NO_HABIT)
        return
    if data[user_id]["day"] == 0:
        log.info(f"Пользователь {user_id} вызвал /skip, но цикл ещё не начат")
        bot.reply_to(message, messages.SKIP_NOT_STARTED(data[user_id]["habit"]))
        return

    data[user_id]["progress"] = ""
    data[user_id]["day"] = 0
    data[user_id]["last_date"] = datetime.date.today().isoformat()
    handler_json.load_data = data
    log.info(f"Пользователь {user_id} сбросил привычку '{data[user_id]['habit']}' через /skip")
    bot.reply_to(message, messages.SKIP_RESET(data[user_id]["habit"]))


# Обработчик команды /progress
@bot.message_handler(commands=['progress'])
def progress(message: types.Message):
    user_id = str(message.chat.id)
    if user_id not in data:
        log.warning(f"Пользователь {user_id} вызвал /progress без привычки")
        bot.reply_to(message, messages.NO_HABIT)
        return

    habit = data[user_id]["habit"]
    if data[user_id]["day"] == 0:
        log.info(f"Пользователь {user_id} запросил прогресс, цикл не начат")
        bot.reply_to(message, messages.PROGRESS_NOT_STARTED(habit))
    else:
        log.info(f"Пользователь {user_id} запросил прогресс: {data[user_id]['progress']} ({data[user_id]['day']}/7)")
        bot.reply_to(message, messages.PROGRESS_INFO(habit, data[user_id]["progress"], data[user_id]["day"]))


if __name__ == "__main__":
    log.info("Bot starting!")
    bot.infinity_polling(skip_pending=True)
