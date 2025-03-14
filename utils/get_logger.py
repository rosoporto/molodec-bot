import logging
from logging.handlers import RotatingFileHandler
from utils.create_path import create_path


# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Уровень логирования


# Создаем форматтер
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Создаем файловый обработчик, который будет записывать логи в файл
log_file_path = create_path("logs", "app.log")

file_handler = RotatingFileHandler(
    log_file_path,
    maxBytes=1024*1024,
    backupCount=5,
    encoding="UTF-8"
)  # 1 MB per file, 5 backups

file_handler.setFormatter(formatter)


# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


# Опционально: можно добавить вывод логов в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
