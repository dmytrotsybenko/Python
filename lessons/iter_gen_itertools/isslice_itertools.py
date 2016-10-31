from itertools import islice


xs = range(10)
print(list(islice(xs, 3)))  # = xs[:3]
print(list(islice(xs, 3, None)))  # = xs[3:]
print(list(islice(xs, 3, 8, 2)))  # = xs[3:8:2]