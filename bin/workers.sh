#!/usr/bin/env bash

# move to project root
cd "$(dirname "$0")"
cd ..

# kill child processes on exit
trap 'kill $(jobs -p)' EXIT

# workers to be run, lines can be repeated
WORKERS=(
    github.fetch_metadata
    github.fetch_repos
    github.fetch_repos
    github.fetch_repos
    github.fetch_repos
    github.fetch_repos
    log.print_logs
)

for worker in "${WORKERS[@]}"
do
    echo "starting $worker"
    python ./bin/run_workers.py sample.ini "$worker" &
done

# run forever
while true; do sleep 86400; done
