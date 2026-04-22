FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# non-root user
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup
RUN chown -R appuser:appgroup /app

USER appuser

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
CMD python -c "import redis; print('ok')" || exit 1

CMD ["python", "worker.py"]
