FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine AS production
WORKDIR /app

# Pin wget version for hadolint DL3018
RUN apk add --no-cache wget=1.24.5-r0 \
    && adduser -D appuser

COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules
RUN chown -R appuser:appuser /app
USER appuser
HEALTHCHECK CMD wget --spider -q http://localhost:3000 || exit 1
CMD ["npm", "app.js"]
