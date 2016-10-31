def import_wrapper(name, *args, imp="__import__"):
    print("importing", name)
    return imp(name, *args)


import builtins
builtins.__import__ = import_wrapper
import collections

