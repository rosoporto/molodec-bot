# MolodecBot

Телеграм-бот "МОЛОДЕЦ" помогает формировать привычки, отслеживая выполнение задач в циклах по 7 дней. За каждый день выполнения добавляется буква в слово "МОЛОДЕЦ". Пропуск дня сбрасывает цикл, а успешное завершение 7 дней подряд отмечается поздравлением.

## Возможности
- Добавление привычки через `/new_habit`.
- Отметка выполнения с `/done`.
- Пропуск дня с `/skip`.
- Просмотр прогресса с `/progress`.
- Логирование действий в `logs/app.log`.
- Хранение данных в `base/users.json`.

## Требования
- Python 3.12+
- Docker (для контейнеризации)
- Git (для работы с репозиторием)

## Установка и запуск локально

### 1. Клонирование репозитория
```bash
git clone https://github.com/<your-username>/molodec-bot.git
cd molodec-bot
```

### 2. Настройка окружения

#### Создай файл `.env` в корне проекта:
```text
TG_TOKEN=your-telegram-bot-token
```
Получи токен у @BotFather в Telegram.

### 3. Установи зависимости:
```bash
pip install -r requirements.txt
```

### 4. Запусти бота:
```bash
make run
```
или на прямую
```bash
python3 -m bot
```

## Запуск в Docker

### 1. Сборка образа:

```bash
docker build -t molodec-bot .
```

### 2. Запуск контейнера:
```bash
docker run --rm -v $(pwd)/base:/app/base -v $(pwd)/logs:/app/logs -v $(pwd)/.env:/app/.env molodec-bot
```

Убедись, что папки `base/` и `logs/` существуют, или создай их:

```bash
mkdir -p base logs
```

### 3. Проверка
Бот должен отвечать в Telegram, а логи записываться в `logs/app.log`.

## Использование Docker Compose
1. Убедись, что `docker-compose.yml` есть в проекте.
2. Запусти:

```bash
docker-compose up --build
```

3. Останови:

```bash
docker-compose down
```

## Тестирование
1. Используй команды: `/new_habit`, `/done`, `/skip`, `/progress`.
2. Проверяй логи в `logs/app.log` и данные в `base/users.json`.

## Связь с автором проекта:
Создано @rosoporo. Свяжитесь через [Telegram](https://t.me/rosoporo)