import time

class Timer:
    def __init__(self):
        self.startTime = 0

    def startTiming(self):
        self.startTime = time.clock()

    def getCurrentTime(self):
        return time.clock() - self.startTime
