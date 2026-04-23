from fastapi import FastAPI
import redis
import uuid
import os
from fastapi.responses import JSONResponse

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)


@app.get("/")
def root():
    return {"message": "api running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/submit")
def create_job():
    job_id = str(uuid.uuid4())
    r.lpush("job", job_id)
    r.hset(f"job:{job_id}", "status", "queued")
    return {"job_id": job_id}


@app.get("/status/{job_id}")
def get_job(job_id: str):
    status = r.hget(f"job:{job_id}", "status")
    if not status:
        return JSONResponse(status_code=404, content={"Error": "not found"})
    return {"job_id": job_id, "status": status}
