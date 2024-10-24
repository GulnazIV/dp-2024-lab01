from lib.SingletonLogger import SingletonLogger

logger1 = SingletonLogger('D:\log1')
logger1.log("er","info 1")
logger1.log("WARN", "warn")

logger2 = SingletonLogger('log')
logger2.log("ERROR", "error")

logger3 = SingletonLogger('log')
logger3.log("INFO", "info 3")
logger3.log("ERROR", "error 3")

# assert logger1 is not logger2