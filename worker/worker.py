import time
import os
import redis


# FIX: Use env variable instead of localhost (works in Docker + local)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)


def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)  # simulate work
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")


while True:
    try:
        job = r.brpop("job", timeout=5)
    except Exception as e:
        print("Redis error:", e)
        continue

    if job:
        _, job_id = job

        try:
            process_job(job_id.decode())
        except Exception as e:
            print("Decode error:", e)
