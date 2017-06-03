#!/usr/bin/env bash

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

# run forever
while true; do sleep 86400; done
