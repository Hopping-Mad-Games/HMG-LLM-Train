#!/usr/bin/env bash
watchfiles --run 'uvicorn ui.reactpy_app.app:fastapi_app --reload --port 8000' .
