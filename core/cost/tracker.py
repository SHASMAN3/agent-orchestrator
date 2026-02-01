from core.cost.model import MODEL_COSTS

class CostTracker:
    def __init__(self, max_usd: float):
        self.max_usd = max_usd
        self.spent = 0.0

    def charge(self, input_tokens: int, output_tokens: int, model: str):
        costs = MODEL_COSTS[model]
        cost = (
            input_tokens * costs["input"] +
            output_tokens * costs["output"]
        )
        self.spent += cost

        if self.spent > self.max_usd:
            raise RuntimeError("Agent budget exceeded")

        return cost
