from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from themachine.core import publish
import inspect
import logging
import os

def log(level, message, *args):
    frame, filename, line_number, function_name, lines, index = inspect.getouterframes(inspect.currentframe())[1]
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
    log(DEBUG, message, *args)

def info(message, *args):
    log(INFO, message, *args)

def warning(message, *args):
    log(WARNING, message, *args)

def error(message, *args):
    log(ERROR, message, *args)

def critical(message, *args):
    log(CRITICAL, message, *args)
