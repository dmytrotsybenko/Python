from functools import wraps


def once(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True
    inner.called = False
    return inner


@once
def identity():
    return print("Called identity func")

identity()
identity()
identity()