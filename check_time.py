import time

class TimeTracker():
    def __init__(self) -> None:
        self.start_time = None
        self.threshold = 5
        
    def start_game(self):
        self.start_time = time.perf_counter()
        
    def get_elapsed_time(self):
        if self.start_time is None:
            raise ValueError("Game not started")
        return time.perf_counter() - self.start_time
    
    def is_game_live(self):
        elapsed_time = self.get_elapsed_time()
        return elapsed_time >= self.threshold
        
