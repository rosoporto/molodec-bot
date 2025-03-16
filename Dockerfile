FROM python:3.12-slim

# Обновление pip и установка зависимостей
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Рабочая директория и копирование кода
WORKDIR /app
COPY . .

# Создание директорий с правильными правами
RUN mkdir -p /app/base /app/logs && chmod -R 777 /app/base /app/logs

# Настройка окружения
ENV PYTHONUNBUFFERED=1

# Запуск бота
CMD ["python3", "bot.py"]