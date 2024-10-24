import threading
import datetime
import os

class SingletonLogger:
    _instance = None
    _lock = threading.Lock()
    # !!!

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(SingletonLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        os.makedirs('log', exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        # !!!
        self.filename = f"log/DP.P1.{timestamp}.log"
        with open(self.filename, 'w'):
            pass


    def log(self, level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{timestamp} [{level}] {message}\n"
        # !!!!
        with self._lock:
            with open(self.filename, 'a') as log_file:
                log_file.write(formatted_message)

# pathlib