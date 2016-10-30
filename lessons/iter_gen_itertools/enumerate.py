def enumerate(iterables, index=0):
    for iterable in iterables:
        yield iterable, index
        # yield index
        index += 1
print(enumerate('abc'))
print(list(next(enumerate('abc'))))
print(list(next(enumerate('abc'))))
print(list(next(enumerate('abc'))))