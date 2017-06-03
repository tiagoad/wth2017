import argparse
import configparser
import importlib
import os
import traceback

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("config", help="ini file with environment variables")
    args = parser.parse_args()

    # load config
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(args.config)

    for key, value in config['GLOBAL'].items():
        os.environ[key] = value

    # run api
    from themachine import api
    api.app.run()

if __name__ == '__main__':
    main()
