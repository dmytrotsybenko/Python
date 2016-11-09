import time
from functools import wraps


def timethis(func):

   @wraps(func)
   def wrapper(*args, **kwargs):
       start = time.time()
       result = func(*args, **kwargs)
       end = time.time()
       print(func.__name__, end - start)
       return result
   return wrapper

@timethis
def countre(n):
    while n > 0:
        n -= 1

countre(10000)