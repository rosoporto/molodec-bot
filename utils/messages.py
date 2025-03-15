from telebot import formatting
from utils.get_logger import logger as log


class Messages:
    WELCOME = formatting.mbold("Привет!") + " 👋 Я бот 'МОЛОДЕЦ'. Добавь привычку с /new_habit!"
    NEW_HABIT_PROMPT = "Напиши свою привычку!👇"
    HABIT_EMPTY = "Привычка не может быть пустой! Попробуй ещё раз с /new_habit"
    NO_HABIT = "Сначала добавь привычку с /new_habit!"

    @staticmethod
    def HABIT_ACCEPTED(habit: str) -> str:
        return f"Привычка '{habit}' принята! Начни с /done, когда сделаешь первый шаг!"

    @staticmethod
    def DONE_START(habit: str) -> str:
        return f"Старт! '{habit}': М ✅⬜⬜⬜⬜⬜⬜ (1/7). Ты молодец!"

    @staticmethod
    def DONE_MISSED(habit: str) -> str:
        return f"Пропуск больше дня! '{habit}' сброшена. Начни заново с /done!"

    @staticmethod
    def DONE_PROGRESS(habit: str, progress: str, day: int) -> str:
        return f"Круто! '{habit}': {progress} {'✅' * day + '⬜' * (7 - day)} ({day}/7). Огонь!"

    @staticmethod
    def DONE_COMPLETE(habit: str) -> str:
        return f"ТЫ СДЕЛАЛ ЭТО! 🎉 '{habit}': МОЛОДЕЦ ✅✅✅✅✅✅✅. Новый цикл — с /done!"

    @staticmethod
    def SKIP_NOT_STARTED(habit: str) -> str:
        return f"Ты ещё не начал '{habit}'! Сделай первый шаг с /done!"

    @staticmethod
    def SKIP_RESET(habit: str) -> str:
        return f"'{habit}' сброшена. Начни заново с /done, когда будешь готов!"

    @staticmethod
    def PROGRESS_NOT_STARTED(habit: str) -> str:
        return f"Привычка: '{habit}'. Пока не начата. Сделай первый шаг с /done!"

    @staticmethod
    def PROGRESS_INFO(habit: str, progress: str, day: int) -> str:
        return f"Привычка: '{habit}'\nПрогресс: {progress} {'✅' * day + '⬜' * (7 - day)} ({day}/7)"


if __name__ == "__main__":
    messages = Messages()
    habit = "Читать книгу по 30 мин."
    log.debug(messages.HABIT_ACCEPTED(habit))
