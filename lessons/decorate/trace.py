def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner 


@trace
def some_func(x):
    return x


some_func(42)