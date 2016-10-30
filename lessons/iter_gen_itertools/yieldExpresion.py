def g():
    res = yield
    print("Got {!r}".format(res))
    res = yield 42
    print("New Got {!r}".format(res))

gen = g()
# next(gen)
# next(gen)
# next(gen)     return None

gen.send(None)  # = next(gen)
gen.send("foobar")