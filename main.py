import click

from consumer import consume_messages
from producer import send_message


@click.group()
def cli():
    pass


@cli.command
@click.option("--kafka", required=True, help="Kafka server (ip:port)")
@click.option("--topic", required=True, help="Kafka topic")
@click.option("--message", required=True, help="Message to send")
def produce(kafka, topic, message):
    send_message(kafka, topic, message)


@cli.command
@click.option("--kafka", required=True, help="Kafka server (ip:port)")
@click.option("--topic", required=True, help="Kafka topic")
def consume(kafka, topic):
    consume_messages(kafka, topic)


if __name__ == "__main__":
    cli()
