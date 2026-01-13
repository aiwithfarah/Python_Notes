# If we search for a number in a list of 10 Million items:
# Linear Search has to check 10,000,000 times (worst case).
# Binary Search checks... about 24 times.

# ------------------CHALLENGE----------------
# Create a massive sorted list: data = list(range(10000000)) (10 Million).
# Target is the last number: 9999999.
# Time the Linear Search (use your old function).
# Time the Binary Search (use your new function).
# Print both times.

import time


def linear_search(arr, x):

    # loop through the length of the list
    for index in range(len(arr)):
        # Check if the ITEM at this index is the target
        if arr[index] == x:
            return index
    return -1


def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        # mid + 1 and mid - 1 to shrink the search zone effectively
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
    return -1


data = list(range(10000000))
target = 9999999

# Race - 1 Linear
start = time.time()
linear_search(data, target)
end = time.time()
print(f'Linear Time: {end - start} seconds')

# Race - 2 Binary
start = time.time()
binary_search(data, target)
end = time.time()
print(f"Binary time: {end - start} seconds")

# Linear Time: 0.3449742794036865 seconds
# Binary time: 1.6450881958007812e-05 seconds
# Your result for Binary Search is 1.64...e-05. The e-05 means "move the decimal point 5 spots to the left."

# Linear Time: 0.3449 seconds

# Binary Time: 0.000016 seconds
# Binary Search was roughly 21,000 times faster!
# If this were a Google search waiting for results:
# Binary Search would feel instant.
# Linear Search would feel like a noticeable lag.
