# .union(other_set): Combines two sets (All items from both). Symbol: |
# .intersection(other_set): Finds items common to both. Symbol: &
# .difference(other_set): Finds items in the first set but not the second. Symbol: -

set_A = {1, 2, 3}
set_B = {3, 4, 5}

print(set_A.union(set_B))  # {1, 2, 3, 4, 5}
print(set_A.intersection(set_B))  # {3}
print(set_A.difference(set_B))  # {1,2}
