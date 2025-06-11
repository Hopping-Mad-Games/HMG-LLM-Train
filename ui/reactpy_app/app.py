#!/usr/bin/env python3
"""Main FastAPI + ReactPy application entry point."""

from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, run

from .components.main_layout import MainLayout

# Create FastAPI app
fastapi_app = FastAPI(
    title="LLM Trainer MVP",
    description="Local-first LLM fine-tuning framework",
    version="0.1.0"
)

@component
def App():
    """Root ReactPy component."""
    return MainLayout()

# Configure ReactPy with FastAPI
configure(fastapi_app, App)

if __name__ == "__main__":
    run(App, host="0.0.0.0", port=8000)
