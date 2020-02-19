# Bu yavas program

import time
from functools import wraps
from decimal import *

def timeit_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()  # time.perf_counter() 'da kullanilabilir.
        func_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print('{0:10}.{1:<8} : {2:<8}'.format(func.__module__, func.__name__, end - start))
        return func_return_val
    return wrapper


@timeit_wrapper
def exp(x):
    getcontext().prec += 2
    i, lasts, s, fact, num = 0,0,1,1,1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -= 2
    return +s

print('{0:<10} {1:<8} {2:^8}'.format('module', 'function', 'time'))
exp(Decimal(150))
exp(Decimal(400))
exp(Decimal(3000))
