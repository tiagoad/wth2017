#!/bin/bash
#
# DEVELOPMENT SCRIPT
# Runs the log.print_logs worker for debugging

# move to project root
cd "$(dirname "$0")"
cd ..

python ./bin/run_workers.py config.ini log.print_logs
