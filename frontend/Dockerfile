# ---------- BUILD STAGE ----------
FROM node:20-alpine3.21 AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .

# ---------- RUNTIME STAGE ----------
FROM node:20-alpine3.21

WORKDIR /app

# create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/. ./

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 3000

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD wget -qO- http://localhost:3000 || exit 1

CMD ["node", "server.js"]
