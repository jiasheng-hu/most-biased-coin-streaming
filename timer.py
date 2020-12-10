import time

class Timer:
    def __init__(self):
        self.startTime = 0

    def startTiming(self):
        self.startTime = time.perf_counter()

    def getCurrentTime(self):
        return time.perf_counter() - self.startTime