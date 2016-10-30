def map(func, iterable, *rest):
    for args in zip(iterable, *rest):
        yield func(*args)


xs = range(5)
print(list(map(lambda x: x *x , xs)))
