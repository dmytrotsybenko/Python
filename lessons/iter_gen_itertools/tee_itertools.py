from itertools import tee

# it = iter(range(3))
it = range(3)
a, b, c = tee(it, 3)
used = list(it)
print(list(a))
print(list(a))
# ------------------

print(list(a))
print(list(b))
print(list(c))

# print(a[0])