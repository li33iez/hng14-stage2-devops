FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM node:20-alpine AS production
WORKDIR /app

RUN apk add --no-cache curl=8.17.0-r1 \
    && adduser -D appuser

COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public

RUN chown -R appuser:appuser /app
USER appuser

HEALTHCHECK --interval=10s --timeout=3s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:3000 || exit 1

EXPOSE 3000
CMD ["npm", "start"]
