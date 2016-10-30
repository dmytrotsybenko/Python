def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item


xs = range(3)
ys = [42]
print(chain(xs, ys))
print(list(chain(xs, ys)))
