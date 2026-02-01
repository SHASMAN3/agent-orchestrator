class ToolLimiter:
    def __init__(self, max_calls: int = 3):
        self.calls = 0
        self.max_calls = max_calls

    def check(self):
        self.calls += 1
        if self.calls > self.max_calls:
            raise RuntimeError("Tool call limit exceeded")

