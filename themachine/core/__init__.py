import pika
import json
import os

MAIN_EXCHANGE='amq.topic'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv('AMQP_URL')))
channel = connection.channel()

def consumer(topic, name=None):
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

def start_consuming():
    channel.start_consuming()

def publish(topic, data):
    channel.basic_publish(
        exchange='amq.topic',
        routing_key=topic.lower(),
        body=json.dumps(data))
