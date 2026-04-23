#!/bin/bash
set -e

echo "Waiting for services to be healthy..."
timeout 120 bash -c 'while ! docker compose ps --format json | jq -e "all(.[]; .Health == \"healthy\" or .Health == \"\")"; do sleep 2; done'

echo "Checking API from inside container..."
docker exec hng14-stage2-devops-api-1 curl -sf http://localhost:8000/health

echo "Checking Frontend from inside container..."
docker exec hng14-stage2-devops-frontend-1 wget --spider -q http://localhost:3000

echo "Integration tests passed"
