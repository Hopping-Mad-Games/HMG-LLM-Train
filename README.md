# LLM Trainer MVP

This repository contains the **minimum‑viable implementation** of a local-first LLM fine‑tuning framework built around a **ReactPy + FastAPI** user interface and a plug‑in oriented backend.

## Quick start (dev)

```bash
git clone <repo-url>
cd llm_trainer_mvp
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
./scripts/dev.sh   # hot‑reload server on http://localhost:8000
```

## Project layout (top-level)

| Path                 | Purpose |
|----------------------|---------|
| `core/`              | Training engine (scheduler, data pipes, trainers, exporters) |
| `ui/`                | ReactPy application plus static assets |
| `plugins/`           | Drop‑in nodes that extend the graph (each in its own directory) |
| `datasets/`          | Sample corpora for smoke tests |
| `docs/`              | Longer‑form architecture & contribution guides |
| `docker/`            | Container and compose files for deployment |
| `scripts/`           | Helper CLI for dev and CI |

For full details see `docs/ARCHITECTURE.md`.

---

## External Documentation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [ReactPy Documentation](https://reactpy.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Python-dotenv Documentation](https://saurabh-kumar.com/python-dotenv/)
- [Python Official Docs](https://docs.python.org/3/)
