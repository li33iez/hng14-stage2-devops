#!/bin/bash
set -e

echo "Starting services..."
docker compose up -d

echo "Waiting for services..."
sleep 15

echo "Containers status:"
docker compose ps

echo "Checking API..."
curl -f http://localhost:8000/health

echo "Checking frontend..."
curl -f http://localhost:3000

echo "Running test job..."
JOB_ID=$(curl -s -X POST http://localhost:8000/submit | grep -o '"job_id":"[^"]*' | cut -d'"' -f4)

curl -f http://localhost:8000/status/$JOB_ID

echo "Success!"

docker compose down -v
