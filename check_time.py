import time

class TimeTracker():
    def __init__(self) -> None:
        pass
    
    def start_timer(self):
        self.start_time = time.perf_counter()
        return self.start_time
        
    def end_timer(self):
        self.end_time = time.perf_counter()
        return self.end_time
        
    def time_elapsed(self):
        if self.start_time is None or self.end_time is None:
            raise ValueError("Timer not started or ended.")
        return self.end_time - self.start_time
        