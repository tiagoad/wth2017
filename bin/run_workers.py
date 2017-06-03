import importlib
import argparse
import configparser
import os

from themachine.core import start_consuming
from themachine import log

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("config", help="ini file with environment variables")
    parser.add_argument('workers', nargs='*', help='worker names')
    args = parser.parse_args()

    # load config
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(args.config)

    for worker in args.workers:
        for section in config.sections():
            if section == 'GLOBAL' or worker.startswith(section):
                for key, value in config[section].items():
                    os.environ[key] = value

        log.log(log.INFO, 'Running worker %s' % worker)
        importlib.import_module('themachine.workers.' + worker)

    while True:
        try:
            start_consuming()
        except Exception as e:
            log.log(log.CRITICAL, 'Worker crashed: %s', e)

if __name__ == '__main__':
    main()
