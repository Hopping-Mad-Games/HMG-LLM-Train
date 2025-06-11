from reactpy import component, html

@component
def LoRATrainerPane():
    return html.div(
        html.h2("LoRA Trainer"),
        html.p("Configure hyper‑parameters and press start.")
    )
