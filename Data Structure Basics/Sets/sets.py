Sets require their items to be "hashable" (immutable). Because a List is mutable (you can change it later),
Python forbids putting a List inside a Set. If you try { [1,2] }, Python throws a TypeError: unhashable type: 'list'.
Fix: You can put a Tuple inside a Set, because Tuples are immutable.



my_set = set()
print(my_set)

my_set.add(1)
print(my_set)  # {1}

print(set([1, 1, 2, 3]))

