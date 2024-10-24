from lib.SingletonLogger import SingletonLogger

logger1 = SingletonLogger('log')
logger1.log("fff","info 1")
logger1.log("WARN", "warn")

logger2 = SingletonLogger('log')
logger2.log("ERROR", "error")

logger3 = SingletonLogger('log')
logger3.log("INFO", "info 3")
logger3.log("ERROR", "error 3")