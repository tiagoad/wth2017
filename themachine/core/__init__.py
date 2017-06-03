import pika
import json
import os

MAIN_EXCHANGE='amq.topic'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv('AMQP_URL')))
channel = connection.channel()

def consumer(topic, name=None):
    """
    Consumer decorator.
    Registers a handler with a topic, and a queue name.
    Once a message is published into the topic it will be redirected to every
    bound queue and processed once by one of the workers subscribed to it.

    :param topic:   Main topic
    :param name:    Queue name

    :return:        Dictionary
    """
    def decorator(function):
        def wrapper(ch, method, properties, body):
            function(json.loads(body))

        result = channel.queue_declare(
            queue=name.lower() if name else '',
            exclusive=True if not name else False)

        channel.queue_bind(
            exchange=MAIN_EXCHANGE,
            queue=result.method.queue,
            routing_key=topic.lower())

        channel.basic_consume(
            wrapper,
            queue=result.method.queue,
            no_ack=True)

    return decorator

def publish(topic, data):
    """
    Publishes a message into a topic.
    Data should be a dictionary

    :param topic:   Topic to publish
    :param data:    Data to send
    """
    channel.basic_publish(
        exchange='amq.topic',
        routing_key=topic.lower(),
        body=json.dumps(data))


def start_consuming():
    """
    Begins the consumer loop.
    """
    channel.start_consuming()
