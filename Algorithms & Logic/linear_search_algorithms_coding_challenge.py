# Challenge 1: The Linear Search
# Define a function search(arr, x).
# Iterate through the list arr.
# If you find x, return the index where it was found.
# If the loop finishes and you haven't found it, return -1.

import time


def linear_search(arr, x):

    # loop through the length of the list
    for index in range(len(arr)):
        # Check if the ITEM at this index is the target
        if arr[index] == x:
            return index
    return -1


# Challenge 2: The Speed Test
# Import the time module.
# Create a massive list: data = list(range(1000000)) (1 million numbers).
# Set target = 999999 (The worst-case scenario: it's at the very end).
# Capture the start time: start = time.time().
# Call your function: linear_search(data, target).
# Capture the end time: end = time.time().
# Print: end - start.


massive_list = list(range(100000000))
x = 9999999

# Start the time
start = time.time()

# Run the search
result = linear_search(massive_list, x)

# Stop the timer
end = time.time()

print(f"Found at index: {result}")
print(f"Time Taken: {end - start} seconds")


# Question: That seems fast, but what if we had 1 Billion users (like Facebook)? 0.05 seconds x 1000 = 50 seconds.
# That is too slow for a website.

# We need an algorithm that is faster than O(n). We need Binary Search. Ready to learn the "Divide and Conquer" trick?
