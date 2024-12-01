from contextlib import contextmanager

from kafka import KafkaProducer

from logger import logger


@contextmanager
def _get_producer(kafka_server):
    try:
        producer = KafkaProducer(bootstrap_servers=kafka_server)
        yield producer
    except Exception as e:
        logger.error(f"Error creating producer: {e}")
    finally:
        producer.close()


def send_message(kafka_server, topic, message):
    with _get_producer(kafka_server) as producer:
        producer.send(topic, message.encode("utf-8"))
        producer.flush()
