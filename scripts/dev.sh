#!/usr/bin/env bash
watchfiles --run 'uvicorn ui.reactpy_app.app:fastapi_app --port 8000 --reload' .
