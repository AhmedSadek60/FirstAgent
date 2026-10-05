#!/usr/bin/env bash
# Start the local LLM chat server on http://localhost:8000
cd "$(dirname "$0")"
. .venv/bin/activate
exec uvicorn server:app --host 0.0.0.0 --port 8000
