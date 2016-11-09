'''import contacts


@pre(lambda _,y: len(y) > 0)
def find_element(elem,list):
    pass

'''
from functools import wraps

def pre(cond, message):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)
        return inner
    return wrapper

@pre(lambda x: x >=0, 'negative arg')
def check_numb(x):
    return x


check_numb(42)
