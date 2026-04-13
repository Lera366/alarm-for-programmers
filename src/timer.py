# Модуль таймера будильника

import time
import threading

class AlarmTimer:
    def __init__(self):
        self.remaining_seconds = 0
        self.is_running = False
    
    def set_timer(self, hours=0, minutes=0, seconds=0):
        self.remaining_seconds = hours * 3600 + minutes * 60 + seconds
    
    def start(self):
        self.is_running = True
        threading.Thread(target=self._countdown).start()
    
    def _countdown(self):
        while self.remaining_seconds > 0 and self.is_running:
            time.sleep(1)
            self.remaining_seconds -= 1
        
        if self.remaining_seconds == 0:
            self._trigger_alarm()
    
    def _trigger_alarm(self):
        print("БУДИЛЬНИК! Время вышло!")
