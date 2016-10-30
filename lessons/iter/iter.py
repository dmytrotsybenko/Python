import math
import urllib
import random
class MyIterClass(object):
    def __init__(self):
        self.rand = random.random()
        print(self.rand)

    def __iter__(self):
        return self
    def next(self):
        if self.arg == " ":
            raise "Its empty string"
        l = int(self.rand * 2)
        return l

    #  raise StopIteration


myiter = MyIterClass()
for x in myiter:
    print(x)
    print("iter iter iter")
# myiter = "qwerty"


