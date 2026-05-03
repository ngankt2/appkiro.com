FROM oven/bun:1 AS deps
WORKDIR /app

COPY package.json bun.lock ./

RUN bun install --frozen-lockfile

FROM deps AS builder
WORKDIR /app

COPY . .

RUN bun run build

FROM oven/bun:1 AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV HOST=0.0.0.0
ENV PORT=3000

COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist

USER bun

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 CMD ["bun", "-e", "fetch('http://127.0.0.1:' + (process.env.PORT || 3000) + '/').then((res) => process.exit(res.ok ? 0 : 1)).catch(() => process.exit(1))"]

CMD ["bun", "run", "start"]
