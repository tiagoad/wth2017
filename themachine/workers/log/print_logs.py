"""
Prints logs into stdout.
"""

from themachine.core import consumer, start_consuming

FORMAT_STRING = '[{levelname}] {module} - {message}'

@consumer(topic='logs.#')
def print_log(data):
    print(FORMAT_STRING.format_map(data))
