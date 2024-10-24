import threading
from datetime import datetime
import os
from module.log_levels import LEVELS

class SingletonLogger:
    """
    Класс логгера, реализованный по шаблону Singleton.
    Обеспечивает потокобезопасную запись логов в файл.
    """
    _instance = None
    _lock_create = threading.Lock()
    _lock_write = threading.Lock()

    def __new__(cls, *args):
        """
        Метод для создания нового экземпляра класса.
        :param args: аргументы, передаваемые при создании экземпляра
        :return: единственный экземпляр класса
        """
        if cls._instance is None:
            with cls._lock_create:
                if cls._instance is None:
                    cls._instance = super(SingletonLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, path_directory):
        """
        Инициализатор класса.
        Создает файл для логов в указанной директории.
        :param path_directory: путь к директории, где будет создан файл логов
        """
        self._create_file(path_directory)
        with open(self.path_file, 'w'):
            pass

    def _create_file(self, path: str):
        """
        Создает файл для логирования.
        Если директория не существует, она будет создана.
        :param path: путь к директории для создания файла логов
        """
        os.makedirs(path, exist_ok=True)
        time_stamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        self.path_file = f"{path}/DP.P1.{time_stamp}.log"


    def log(self, level: LEVELS, message: str):
        """
        Записывает сообщение в файл лога с указанным уровнем важности.
        :param level: уровень важности сообщения
        :param message: текст сообщения для записи в лог
        """
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{time_stamp} [{level.value}] {message}"
        with self._lock_write:
            with open(self.path_file, 'a') as log_file:
                log_file.write(formatted_message + '\n')
