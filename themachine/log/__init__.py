from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from themachine.core import publish
import inspect
import logging

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

        'message': message % args
    })
