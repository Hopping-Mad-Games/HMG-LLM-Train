# 🏗️ Architecture

```
ReactPy UI ↔ FastAPI  ← in‑proc →  Core Engine  ← plugin hook → plugins/
```

## Overview

This project is a local-first, plugin-driven LLM fine-tuning framework.  
We intentionally **build on proven open-source solutions** for each layer, adapting and extending them as needed.

---

## Upstream Projects & Inspirations

| Project | Repository | License | Usage/Reference |
|---------|------------|---------|-----------------|
| **ReactPy** | [github.com/reactive-python/reactpy](https://github.com/reactive-python/reactpy) | MIT | UI framework; see [`ui/reactpy_app/`](../ui/reactpy_app/) |
| **FastAPI** | [github.com/tiangolo/fastapi](https://github.com/tiangolo/fastapi) | MIT | API backend; see [`ui/reactpy_app/app.py`](../ui/reactpy_app/app.py) |
| **LLaMA-Factory** | [github.com/hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | Apache-2.0 | Hyperparameter presets, LoRA/QLoRA training patterns, optimizer strategies (GaLore, APOLLO, BAdam, Muon), quantization, and distributed training support. Influences [`plugins/lora_trainer/`](../plugins/lora_trainer/) design and capabilities. |
| **text-generation-webui** | [github.com/oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) | AGPL-3.0 | Adapter merge UX, plugin system architecture inspiration (see [`plugins/`](../plugins/)). |
| **ComfyUI** | [github.com/comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI) | MIT | Node-graph UI/UX patterns for workflow definition. |
| **react-flow** | [github.com/wbkd/react-flow](https://github.com/wbkd/react-flow) | MIT | Node graph rendering (used via ReactPy integration). |
| **d3-force** | [github.com/d3/d3-force](https://github.com/d3/d3-force) | BSD-3 | Graph layout algorithms (used via ReactPy integration). |
| **peft** | [github.com/huggingface/peft](https://github.com/huggingface/peft) | Apache-2.0 | Core library for Parameter-Efficient Fine-Tuning techniques like LoRA, QLoRA, DoRA, PiSSA, OLoRA, LoftQ, X-LoRA, AdaLoRA. Used in [`plugins/lora_trainer/backend.py`](../plugins/lora_trainer/backend.py) for adapter configuration, initialization, merging, and multi-adapter inference. |
| **bitsandbytes** | [github.com/TimDettmers/bitsandbytes](https://github.com/TimDettmers/bitsandbytes) | MIT | Enables 8-bit and 4-bit quantization for model parameters, reducing memory footprint. Integrated within the LoRA training plugin ([`plugins/lora_trainer/backend.py`](../plugins/lora_trainer/backend.py)) in conjunction with PEFT. |
| **accelerate** | [github.com/huggingface/accelerate](https://github.com/huggingface/accelerate) | Apache-2.0 | Facilitates multi-GPU, distributed, and mixed-precision training (FSDP, DeepSpeed). The core engine and training plugins leverage Accelerate for scaling training jobs. |
| **watchfiles** | [github.com/samuelcolvin/watchfiles](https://github.com/samuelcolvin/watchfiles) | MIT | Hot-reload dev loop (see [`requirements.txt`](../requirements.txt)). |
| **uvicorn** | [www.uvicorn.org](https://www.uvicorn.org/) | BSD-3-Clause | ASGI server for FastAPI (see [`requirements.txt`](../requirements.txt)). |


---

## Integration Details

### UI Layer

- **ReactPy** is used for all UI components ([`ui/reactpy_app/`](../ui/reactpy_app/)).
- The UI design, particularly for defining and managing training workflows, draws inspiration from the node-graph paradigms of [ComfyUI](https://github.com/comfyanonymous/ComfyUI) and utilizes [react-flow](https://github.com/wbkd/react-flow) (via ReactPy) for rendering.
- Styling is managed via [`ui/assets/styles/main.css`](../ui/assets/styles/main.css).

### Backend/API

- **FastAPI** ([`ui/reactpy_app/app.py`](../ui/reactpy_app/app.py)) serves the ReactPy UI and provides API endpoints for communication between the frontend and the core engine/plugins.
- Development workflow benefits from hot-reloading enabled by **watchfiles** and **uvicorn**.

### Core Engine & LLM Training

The [`core/`](../core/) engine is designed to be modular, orchestrating training tasks and leveraging specialized plugins for specific functionalities. The LLM training capabilities are heavily influenced and built upon several key open-source projects:

-   **Parameter-Efficient Fine-Tuning (PEFT):**
    -   The **`huggingface/peft`** library is a cornerstone for implementing various PEFT methods. This project utilizes `peft` within the [`plugins/lora_trainer/backend.py`](../plugins/lora_trainer/backend.py) for techniques such as:
        -   **LoRA (Low-Rank Adaptation):** Adapting pretrained models by training a small number of new weights (adapter matrices).
        -   **QLoRA:** Further optimizing LoRA by quantizing the pretrained model to 4-bit, loading it into memory, and then attaching LoRA adapters.
        -   Other advanced techniques available in `peft` (like DoRA, PiSSA, OLoRA, LoftQ, X-LoRA, AdaLoRA) can be incorporated via `PeftConfig` and model initialization options.
    -   The system supports adapter merging and multi-adapter inference, allowing for flexible model composition post-training, drawing from `peft`'s capabilities.

-   **Quantization with `bitsandbytes`:**
    -   To manage memory constraints and enable training larger models on consumer hardware, **`TimDettmers/bitsandbytes`** is used for 8-bit and 4-bit quantization of model parameters.
    -   This is typically applied in conjunction with QLoRA within the [`plugins/lora_trainer/backend.py`](../plugins/lora_trainer/backend.py), where `BitsAndBytesConfig` from `transformers` (which interfaces with `bitsandbytes`) is used during model loading.

-   **Training Orchestration & Optimization (Inspired by `LLaMA-Factory`):**
    -   While not a direct dependency, **`hiyouga/LLaMA-Factory`** serves as a significant source of inspiration for the training process within [`plugins/lora_trainer/`](../plugins/lora_trainer/). This includes:
        -   **Hyperparameter Presets:** Adopting well-tested hyperparameter configurations for various models and datasets.
        -   **LoRA/QLoRA Training Patterns:** Structuring the training loop, data handling, and adapter saving/loading mechanisms.
        -   **Optimizer Strategies:** Potentially incorporating advanced optimizer variants showcased in LLaMA-Factory (e.g., GaLore, APOLLO, BAdam, Muon) if beneficial for specific training scenarios.
        -   **Dataset Handling:** LLaMA-Factory provides robust dataset processing and formatting, which can inform the data preprocessing steps in this project.

-   **Distributed Training with `accelerate`:**
    -   **`huggingface/accelerate`** is employed to simplify and manage distributed training across multiple GPUs and for mixed-precision training.
    -   It handles the complexities of different distributed setups (e.g., FSDP, DeepSpeed) with minimal code changes in the training scripts (likely within the `core` engine or invoked by plugins like `lora_trainer`).
    -   `Accelerate`'s `Accelerator` object is used to prepare models, optimizers, and dataloaders for the distributed environment.

### Plugins

- The plugin system, located in [`plugins/`](../plugins/), is architecturally inspired by the extensibility of **`oobabooga/text-generation-webui`**.
- Each plugin (e.g., [`plugins/lora_trainer/`](../plugins/lora_trainer/)) is designed to be a self-contained unit, typically including:
    -   A `manifest.yaml` file (e.g., [`plugins/lora_trainer/manifest.yaml`](../plugins/lora_trainer/manifest.yaml)) describing the plugin, its capabilities, and entry points.
    -   A backend module (e.g., [`plugins/lora_trainer/backend.py`](../plugins/lora_trainer/backend.py)) containing the core logic, often interfacing with libraries like `peft`, `bitsandbytes`, and `accelerate`.
    -   An optional UI component (e.g., [`plugins/lora_trainer/ui_component.py`](../plugins/lora_trainer/ui_component.py)) for exposing plugin-specific settings or actions in the ReactPy interface.
- The plugin design allows for easy addition of new training methods, data processors, or utility functions without modifying the core engine extensively.
- The user experience for managing and interacting with plugins, especially for tasks like merging LoRA adapters, draws inspiration from the intuitive interface of `text-generation-webui`.

---

## File/Module References

- **UI Entrypoint:** [`ui/reactpy_app/app.py`](../ui/reactpy_app/app.py)
- **Main Layout:** [`ui/reactpy_app/components/main_layout.py`](../ui/reactpy_app/components/main_layout.py)
- **LoRA Trainer Plugin:** [`plugins/lora_trainer/backend.py`](../plugins/lora_trainer/backend.py), [`plugins/lora_trainer/ui_component.py`](../plugins/lora_trainer/ui_component.py)
- **Plugin Manifest Example:** [`plugins/lora_trainer/manifest.yaml`](../plugins/lora_trainer/manifest.yaml)
- **Core Engine Directory:** [`core/`](../core/)
- **Plugins Directory:** [`plugins/`](../plugins/)
- **Requirements File:** [`requirements.txt`](../requirements.txt)

---

## Notes

- No code is copied verbatim from upstream projects; all integrations are original or adapted with attribution.
- See [`THIRDPARTY.md`](../THIRDPARTY.md) for a full dependency and license table.

See code comments for further details on implementation and adaptation.
