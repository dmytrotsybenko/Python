'''empty_set = set()
empty_set = {1,2,3,4 }
print(empty_set)
'''
first_set = {1,2,3,4,5}
second_set = {1,2,3,5,6,8}
print(first_set & second_set)

print(first_set.union(second_set))
print(first_set - second_set)
print(second_set - first_set)