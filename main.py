import click

from consumer import consume_messages
from producer import send_message
from logger import logger


@click.group()
def cli():
    pass


@cli.command
@click.option("--kafka", required=True, help="Kafka server (ip:port)")
@click.option("--topic", required=True, help="Kafka topic")
@click.option("--message", required=True, help="Message to send")
def produce(kafka, topic, message):
    try:
        send_message(kafka, topic, message)
    except Exception as e:
        logger.error(f"Error sending message: {e}")


@cli.command
@click.option("--kafka", required=True, help="Kafka server (ip:port)")
@click.option("--topic", required=True, help="Kafka topic")
def consume(kafka, topic):
    try:
        consume_messages(kafka, topic)
    except Exception as e:
        logger.error(f"Error consuming messages: {e}")


if __name__ == "__main__":
    cli()
