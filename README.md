# Kafka CLI Application

CLI для Apache Kafka.

## Компоненты

### Producer
Файл: `producer.py`
- Отправка сообщений с `KafkaProducer`
- Контекстный менеджер для управления ресурсами
- Функция `send_message()` для отправки сообщения

### Consumer
Файл: `consumer.py`
- Получение сообщений с `KafkaConsumer`
- Контекстный менеджер для управления ресурсами
- Функция `consume_messages()` для вывода сообщений

### CLI
Файл: `main.py`
- `produce`: Отправка сообщения
- `consume`: Чтение сообщений


## Использование

### Запуск

`docker compose up -d`

### Отправка сообщений

`docker compose run cli produce --kafka kafka:9092 --topic hello --message "Hello, World"`

### Получение сообщений

`docker compose run cli consume --kafka kafka:9092 --topic hello`