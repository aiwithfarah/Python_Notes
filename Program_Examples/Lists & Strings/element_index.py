# find the location of a given element inside a list:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = int(input("Enter a num who's index you want to find: "))
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print(f"Element is found at index {i}")
else:
    print("Absent")
