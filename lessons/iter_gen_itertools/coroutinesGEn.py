def grep(pattern):
    print("Looking for {!r}".format(pattern))
    while True:
        line = yield
        if pattern in line:
            print(line)

gen = grep("Gotcha!")
next(gen)
print(gen.send("This empty line"))
print(gen.send("This line have Gotcha!"))