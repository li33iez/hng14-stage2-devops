WORKER FILE


BUG - (line 6) ; Breaks in Docker (because Redis runs in another container)
		r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

FIX - r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379), 
#       Use env variable instead of localhost 

BUG - line job = r.brpop("job", timeout=5)
FIX - (line 15)
#	 job = r.brpop("job", timeout=5)
#   except Exception as e:
#       print("Redis error:", e)
#       continue
#
#	FIX: Wrap Redis call to prevent crash if Redis is down and easy debugging


BUG - (line 17) - redis error might cause process to crash, Due to invalid decode of error
#	     _, job_id = job
#        process_job(job_id.decode())


FIX -	 process_job(job_id.decode())
#        except Exception as e:
#            print("Decode error:", e)
#	the fix help to do proper decode of error ro prevent crash



API FILE




BUG - (line 8) ; Breaks in Docker (because Redis runs in another container)
#		r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

FIX - r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379),
#       Use env variable instead of localhost


BUG - (line 20) ; Incorrect Redis status check
#		Used `if not status` which incorrectly treated valid values as missing.


FIX -		Replaced with `if status is None`.
#		Redis returns `None` for missing keys, so this is the only reliable check. 





Frontend app.js

BUG - (line 6 ) ; URL hardcoded
#


FIX - const API_URL = process.env.API_URL;
#       const PORT = process.env.PORT;

#	add port and URL to env
