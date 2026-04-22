# ---------- BUILD STAGE ----------
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .

# ---------- RUNTIME STAGE ----------
FROM node:18-alpine

WORKDIR /app

# create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --from=builder /app /app

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 3000

# HEALTHCHECK: ensures container is alive
HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
CMD wget -qO- http://localhost:3000 || exit 1

CMD ["node", "app.js"]
