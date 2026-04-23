FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app

# install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# create a non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# copy deps to appuser home, not /root
COPY --from=builder /root/.local /home/appuser/.local
COPY . .

RUN chown -R appuser:appgroup /app
ENV PATH=/home/appuser/.local/bin:$PATH

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=3s --retries=5 \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

