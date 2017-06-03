These are scripts used for development and debugging

`add_user.py` - Pushes a hardcoded user into the task queue to be processed

`run_workers.py` - Accepts a configuration file (with environment variables) and a list of workers. These workers will be run in the same thread
 
`workers.sh` - Starts a list of workers in different processes for development

`services.sh` - Starts the service dependencies for the project
