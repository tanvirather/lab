#! /bin/bash

cd "$(dirname "$0")" # set path to current folder
docker container rm dockeragent --force # remove existing container if it exists
docker build --tag dockeragent . # build the docker image
docker run --detach --name dockeragent --env-file secrets.env dockeragent # run the container in detached mode
