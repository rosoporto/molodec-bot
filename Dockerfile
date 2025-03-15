FROM python:3.12-slim

# Создание пользователя и группы
RUN groupadd -r groupbots && useradd -r -g groupbots botbreeder

# Обновление pip и установка зависимостей
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Рабочая директория и копирование кода
WORKDIR /app
COPY . .

# Права для пользователя
RUN chown -R botbreeder:groupbots /app
USER botbreeder

# Настройка окружения
ENV PYTHONUNBUFFERED=1

# Определение точек монтирования
VOLUME ["/app/base", "/app/logs", "/app/.env"]

# Запуск бота
CMD ["python3", "bot.py"]