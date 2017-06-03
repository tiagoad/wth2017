from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from themachine.core import publish
import inspect
import logging
import os

def __log(level, message, *args):
    """
    Logs a message into the logs.<level> topic

    :param level:   Log level. Should be one of the constants defined in this module
    :param message: Log message
    :param args:    Message formatting items
    """
    frame, filename, line_number, function_name, lines, index = inspect.getouterframes(inspect.currentframe())[2]
    module = inspect.getmodule(frame)

    publish('logs.%s' % level, {
        'filename': filename,
        'funcName': function_name,
        'levelname': logging.getLevelName(level),
        'levelno': level,
        'lineno': line_number,
        'module': module.__name__,
        'pid': os.getpid(),

        'message': message % args
    })

def debug(message, *args):
    """
    Sends a DEBUG level message

    :param message: Log message
    :param args:    Formatting items
    :return:
    """
    __log(DEBUG, message, *args)

def info(message, *args):
    """
    Sends a INFO level message

    :param message: Log message
    :param args:    Formatting items
    :return:
    """

    __log(INFO, message, *args)

def warning(message, *args):
    """
    Sends a WARNING level message

    :param message: Log message
    :param args:    Formatting items
    :return:
    """

    __log(WARNING, message, *args)

def error(message, *args):
    """
    Sends a ERROR level message

    :param message: Log message
    :param args:    Formatting items
    :return:
    """

    __log(ERROR, message, *args)

def critical(message, *args):
    """
    Sends a CRITICAL level message

    :param message: Log message
    :param args:    Formatting items
    :return:
    """

    __log(CRITICAL, message, *args)
