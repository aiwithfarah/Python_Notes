# If you have a list list_1, then the following assignment: list_2 = list_1 does not make a copy of the list_1 list,
# but makes the variables list_1 and list_2 point to one and the same list in memory.

vehicle = ["car", "bicycle", "motorbike"]
vehicle_two = vehicle

del vehicle[0]
print(vehicle_two)  # ['bicycle', 'motorbike']
