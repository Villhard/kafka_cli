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