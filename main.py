from lib.singleton_logger import SingletonLogger
from module.log_levels import LEVELS

logger1 = SingletonLogger('log')
logger1.log(LEVELS.INFO,"info 1")
logger1.log(LEVELS.WARN, "warn")

logger2 = SingletonLogger('log')
logger2.log(LEVELS.ERROR, "error")

logger3 = SingletonLogger('log')
logger3.log(LEVELS.INFO, "info 3")
logger3.log(LEVELS.ERROR, "error 3")