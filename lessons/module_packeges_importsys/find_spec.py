def find_spec():
    import sys
    builtin_finder, _, path_finder = sys.meta_path
    print(builtin_finder,find_spec("itertools"))
    builtin_finder.find_spec("enum")
    print(path_finder.find_spec("enum"))