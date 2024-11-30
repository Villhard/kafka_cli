from contextlib import contextmanager
from kafka import KafkaProducer


@contextmanager
def _get_producer(kafka_server):
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    try:
        yield producer
    finally:
        producer.close()


def send_message(kafka_server, topic, message):
    with _get_producer(kafka_server) as producer:
        producer.send(topic, message)
        producer.flush()
