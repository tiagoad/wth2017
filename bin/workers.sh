#!/usr/bin/env bash
#
# DEVELOPMENT SCRIPT
# Runs a list of workers in different processes. The workers are killed once the process exits.


# move to project root
cd "$(dirname "$0")"
cd ..

# kill child processes on exit
trap 'kill -9 $(jobs -p)' EXIT

# workers to be run, lines can be repeated
WORKERS=(
    log.print_logs
    github.fetch_metadata
    github.fetch_repos
    github.fetch_repos
    github.fetch_repos
    github.fetch_repos
    github.fetch_repos
    analysis.bandit
    analysis.pep8
)

for worker in "${WORKERS[@]}"
do
    echo "Starting $worker"
    python ./bin/run_workers.py config.ini "$worker" &
done

# run forever (sleep forever doesn't work on BSD-like systems
while true; do sleep 86400; done
