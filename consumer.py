from contextlib import contextmanager

from kafka import KafkaConsumer

from logger import logger


@contextmanager
def _get_consumer(kafka_server, topic):
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=kafka_server,
            group_id="default",
            auto_offset_reset="earliest",
            enable_auto_commit=True,
        )
        yield consumer
    except Exception as e:
        logger.error(f"Error creating consumer: {e}")
    finally:
        consumer.close()


def consume_messages(kafka_server, topic):
    with _get_consumer(kafka_server, topic) as consumer:
        for message in consumer:
            logger.info(message.value.decode("utf-8"))
