These are scripts used for development and debugging

`add_user.py` - Pushes a hardcoded user into the task queue to be processed

`print_logs.sh` - Prints all logs from RabbitHQ into stdout

`run_api.py` - Accepts a configuration file (with environment variables), starts an API server

`run_workers.py` - Accepts a configuration file (with environment variables) and a list of workers. These workers will be run in the same thread
 
`services.sh` - Starts the service dependencies for the project
 
`workers.sh` - Starts a list of workers in different processes for development
