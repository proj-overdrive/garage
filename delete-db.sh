#!/bin/sh

docker compose -f docker-compose.yml down
docker volume rm garage_db
