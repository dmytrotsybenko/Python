def first_gen():
    yield 42
    return "Tail in first gen"


def main_gen():
    res = yield from first_gen()
    print("Got {!r}".format(res))


gen = main_gen()
print(next(gen))
print(next(gen, None))
