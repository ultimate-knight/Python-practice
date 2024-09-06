#here we learn about Function caching#
import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    print(n*7)


fx(20)
print('done after 20')
fx(4)
print('done after 4')
fx(90)
print('done after 90')
fx(30)
print('done after 30')




fx(20)
print('done after 20')
fx(4)
print('done after 4')
fx(90)
print('done after 90')
fx(37)
print('done after 30')