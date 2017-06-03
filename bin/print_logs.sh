#!/bin/bash

# move to project root
cd "$(dirname "$0")"
cd ..

python ./bin/run_workers.py config.ini log.print_logs
