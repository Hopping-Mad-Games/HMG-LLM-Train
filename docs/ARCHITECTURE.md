# Architecture

## Overview
The system is divided into **three loosely‑coupled layers**:

1. **Core engine** – pure Python; orchestrates datasets, tokenization, training loops and exports. Uses `accelerate`, `peft`, and `bitsandbytes`.
2. **UI layer** – a ReactPy SPA mounted inside FastAPI; communicates with the core via in‑process method calls and `asyncio.Queue`.
3. **Plug‑in layer** – optional directories in `plugins/` that register both backend nodes and small ReactPy panels through a `manifest.yaml`.

![diagram](../docs/img/architecture_diagram.png)

## Data flow
```text
  JSONL → DatasetNode → TokenizerNode → LoRATrainer → GGUFExport → artifacts/
```

## Extensibility
Any new feature lives in its own directory under `plugins/`:

```
plugins/
  my_feature/
    backend.py
    ui_component.py
    manifest.yaml
```

On startup the plug‑in loader scans these manifests, imports the Python modules, and mounts UI components into pre‑defined slots in the graph canvas.
