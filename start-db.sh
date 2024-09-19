#!/bin/sh

docker compose -f docker-compose.yml up -d
docker logs -f garage-flyway-1
