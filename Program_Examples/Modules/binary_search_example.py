# Write binary_search(arr, target).
# Use the low, high, and mid logic.
# Remember the while loop condition (low <= high).
# Remember to move the pointers (mid + 1 or mid - 1).
# Show me the code! ⚔️

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1

    return -1


my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(binary_search(my_list, 16))
