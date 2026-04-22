#!/bin/bash
set -e

echo "Starting all services..."
timeout 60s docker compose up -d --wait

echo "Checking frontend..."
curl -f http://localhost:3000

echo "Checking API..."
curl -f http://localhost:8000/status

echo "Integration tests passed"
