# hng14-stage2-devops
# Full Stack Microservices Application

This project is a containerized microservices system consisting of:
- Frontend service
- API service
- Worker service
- Redis (message broker / cache)

All services are orchestrated using Docker Compose.

---

##  Architecture Overview

The system follows this flow:

Frontend → API → Redis → Worker → Redis → API → Frontend

- The **Frontend** sends requests to the API
- The **API** processes requests and communicates with Redis
- The **Worker** consumes jobs from Redis and processes background tasks
- Redis acts as a message broker between services

---

##  Prerequisites

Ensure the following are installed on a clean machine:

- Docker (>= 20.x)
- Docker Compose (v2+)
- Git

### Verify installation

```bash
docker --version
docker compose version
git --version


