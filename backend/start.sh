#!/bin/sh
set -e
alembic -c /app/backend/alembic.ini upgrade head
exec uvicorn app.main:app --app-dir /app/backend --host 0.0.0.0 --port "${PORT:-8000}"
