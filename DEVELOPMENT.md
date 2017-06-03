# Setting up the development environment

## Requirements

- Python 3.6.1
- MongoDB
- RabbitHQ
- tmux (to use the `services.sh` script)

## Install

1. `pip install -r requirements.txt`

2. `pip install --editable .`

## Running

1. Start all the services by running `./bin/services.sh`
 
2. Start workers by running `./bin/workers.sh`

3. Send a test job by running `python ./bin/add_user.py <github user>`
