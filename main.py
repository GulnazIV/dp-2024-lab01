from lib.SingletonLogger import SingletonLogger

logger1 = SingletonLogger()
logger1.log("INFO","info 1")
logger1.log("WARN", "warn")

logger2 = SingletonLogger()
logger2.log("ERROR", "error")

logger3 = SingletonLogger()
logger3.log("INFO", "info 3")
logger3.log("ERROR", "error 3")