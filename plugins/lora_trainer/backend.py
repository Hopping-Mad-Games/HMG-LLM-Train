class LoRATrainerNode:
    """Placeholder backend node for LoRA training."""

    def __init__(self, **kwargs):
        self.params = kwargs

    def run(self, dataloader):
        # Training loop would go here
        return {"status": "ok"}
