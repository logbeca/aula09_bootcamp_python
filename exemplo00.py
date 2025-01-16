from utils_log import log_decorator
from time_decorator import time_measure_decorator
from tenacity_decorator import retry
#from loguru import logger
#print -> logger.imfo
#logger.add("meu_log.log")
@log_decorator
@time_measure_decorator
@retry
 # use as funções do log decator
def soma(x, y):
    x = int(x)
    y = int(y)
    soma = x + y
    return soma

soma(2,"1")
soma(2,8)

## decorator empacota várias funções