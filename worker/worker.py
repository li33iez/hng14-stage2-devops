import redis
import time
import os
import signal

# FIX: Use env variable instead of localhost (works in Docker + local)
# Breaks in Docker (because Redis runs in another container)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)


def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)  # simulate work
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")


while True:
    try:
        # FIX: Wrap Redis call to prevent crash if Redis is down and easy debugging
        job = r.brpop("job", timeout=5)
    except Exception as e:
        print("Redis error:", e)
        continue

    if job:
        _, job_id = job

        try:
            # FIX: Decode safely in case of bad data
            process_job(job_id.decode())
        except Exception as e:
            print("Decode error:", e)
