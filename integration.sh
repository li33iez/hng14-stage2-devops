#!/bin/bash
set -e

echo "Waiting for services to be healthy..."

for i in {1..30}; do
  if docker compose ps | grep -q "(unhealthy)"; then
    echo "Still starting services..."
    docker compose ps
    sleep 30
  else
    echo "Services look healthy"
    docker compose ps
    break
  fi
done

echo "Checking API from inside container..."
docker exec hng14-stage2-devops-api-1 curl -sf http://localhost:8000/health

echo "Checking Frontend from inside container..."
docker exec hng14-stage2-devops-frontend-1 curl -f http://localhost:3000

echo "Integration tests passed"
