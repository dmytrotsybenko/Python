def unique(iterable, seen=None):
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


xs = [1, 1, 2, 3, 5]
print(list(unique(xs)))
print(1 in unique(xs))
