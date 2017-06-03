"""
Prints logs into stdout.
"""

from themachine.core import consumer, start_consuming

FORMAT_STRING = '[{levelname}] PID-{pid} {module} - {message}'

@consumer(topic='logs.#')
def print_log(data):
    """
    Log consumer.
    Prints every log line into the standard output.

    :param data:    Log message, see themachine.log for more information
    """
    print(FORMAT_STRING.format_map(data))
