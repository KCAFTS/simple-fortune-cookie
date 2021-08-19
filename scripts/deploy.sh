#! /usr/bin/env sh
echo Deploying
docker-compose down -v && docker-compose up --build -d
echo Deployed
