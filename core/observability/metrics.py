import time

class Metrics:
    def __init__(self):
        self.counters = {}
        self.timings = {}

    def incr(self, name):
        self.counters[name] = self.counters.get(name, 0) + 1

    def timing(self, name, duration):
        self.timings.setdefault(name, []).append(duration)

metrics = Metrics()
    