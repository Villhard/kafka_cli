from contextlib import contextmanager
from kafka import KafkaConsumer


@contextmanager
def _get_consumer(kafka_server, topic):
    consumer = KafkaConsumer(topic, bootstrap_servers=kafka_server)
    try:
        yield consumer
    finally:
        consumer.close()


def consume_messages(kafka_server, topic):
    with _get_consumer(kafka_server, topic) as consumer:
        for message in consumer:
            print(message.value.decode('utf-8'))
