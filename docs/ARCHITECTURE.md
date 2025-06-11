# 🏗️ Architecture

```
ReactPy UI ↔ FastAPI  ← in‑proc →  Core Engine  ← plugin hook → plugins/
```

*Scheduler* coordinates DAG execution; nodes stream artefacts via async queues.  
See code comments for deep dive.
