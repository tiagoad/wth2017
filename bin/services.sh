#!/bin/bash

# tmux session name
SESSION_NAME=themachine-services

# service command list
SERVICES=(
    "rabbitmq-server"
    "mongod --config /usr/local/etc/mongod.conf"
)

# stop rabbitmq
rabbitmqctl stop

# create a tmux session
tmux new-session -d -s "$SESSION_NAME"

# add the services to the tmux session as windows
i=1
for service in "${SERVICES[@]}"
do
    tmux new-window -t "$SESSION_NAME:$i"
    tmux send-keys -t "$SESSION_NAME:$i" "$service" C-m
    let "i+=1"
done

# attach to the tmux session
tmux select-window -t "$SESSION_NAME:1"
tmux attach-session -t "$SESSION_NAME"
