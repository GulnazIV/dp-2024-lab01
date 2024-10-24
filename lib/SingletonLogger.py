import threading
from datetime import datetime
import os
from enum import Enum

class LogLevel(Enum):
    TRACE = 'TRACE'
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    FATAL = 'FATAL'


class SingletonLogger:

    _instance = None
    _lock_create = threading.Lock()
    _lock_write = threading.Lock()

    def __new__(cls, *args):
        if cls._instance is None:
            with cls._lock_create:
                if cls._instance is None:
                    cls._instance = super(SingletonLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, path):
        self._create_file(path)
        with open(self.file_path, 'w'):
            pass

    def _create_file(self, path):
        os.makedirs(path, exist_ok=True)
        time_stamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        self.file_path = f"{path}/DP.P1.{time_stamp}.log"

    def log(self, level, message):
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level_upper = level.upper()

        try:
            LogLevel[level_upper]
        except KeyError:
            print(f"Ошибка: Уровень {level} не является допустимым")
            print(f"Сообщение {time_stamp} [{level}] {message} не внесено в {self.file_path}")
            return

        formatted_message = f"{time_stamp} [{level_upper}] {message}"
        with self._lock_write:
            with open(self.file_path, 'a') as log_file:
                log_file.write(formatted_message + '\n')
