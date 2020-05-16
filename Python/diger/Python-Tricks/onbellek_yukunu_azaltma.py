import functools
import time

# 12'ye kadar onbellege izin vermek icin:

@functools.lru_cache(maxsize=12)
def slow_func(x):
    time.sleep(2)
    return x

for i in range(0,20):
    slow_func(i)

# program ard arda slow_func'i cagiracak. Bu durumda on bellege yuklenme yapmis olacak. Biz ise lru_cache sayesinde on bellege en fazla 12 tane yuk verilebilecegini belirtiyoruz.
