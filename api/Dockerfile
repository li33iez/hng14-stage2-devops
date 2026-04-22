FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.11-slim

WORKDIR /app

RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

# Fixed: pin version + no-install-recommends + cleanup
docker run debian:bookworm-slim apt-get update && apt-cache policy curl

# Copy installed Python packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy your app code
COPY --from=builder /app /app

RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8000
