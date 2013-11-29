l1 = [1, 2, 3, 4, 5]
l2 = [9, 8, 7, 6, 5]

only_in_l1 = set(l1).difference(l2)
only_in_l2 = set(l2).difference(l1)

# http://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
print("These are in l1 but not in l2:")
for i in only_in_l1:
    print(i)

print("These are in l2 but not in l1:")
for i in only_in_l2:
    print(i)
