# 🦙 LLM Trainer MVP (AGPL‑3.0)

A local‑first, plug‑in‑driven fine‑tuning framework for text and vision LLMs.  
ReactPy front‑end · FastAPI back‑end · LoRA / QLoRA inside · One‑command Docker deploy.

---

## ✨ Features

* Drag‑and‑drop **node graph UI** (ReactPy + react‑flow).  
* **Dataset → Tokenize → Train → Export** pipeline, LoRA by default.  
* Hot‑reload dev loop (`watchfiles` + `uvicorn`).  
* Docker Compose for NVIDIA, ROCm & CPU.  
* Fully **AGPL‑3.0**; every improvement must stay open.

---

## Quick‑start

```bash
git clone https://github.com/you/llm_trainer.git
cd llm_trainer
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
./scripts/dev.sh
```

Open <http://localhost:8000>.

---

## 📜 License & attributions

This repository is **AGPL‑3.0‑or‑later**.  
Design elements were inspired by (but no code copied from):

| Project | License | Idea borrowed |
|---------|---------|---------------|
| LLaMA‑Factory | Apache‑2.0 | Hyper‑param presets |
| text‑generation‑webui | AGPL‑3.0 | Adapter merge UX |
| ComfyUI | MIT | Node‑graph UI |

Third‑party packages and their licenses are cataloged in **THIRDPARTY.md**.
