# BINARY SEARCH: This is the algorithm that powers databases, search engines,
# and why Google can search billions of pages in 0.00001 seconds.

# 1. The Concept: "Divide and Conquer"
# Imagine I ask you to find the page number for "Python" in a dictionary.
# Linear Search: You start at page 1... A... B... C... (This takes forever).
# Binary Search: You open the book exactly in the middle.
# You see the letter "M".
# You know "P" comes after "M".
# Action: You rip the first half of the book (A-M) and throw it in the trash. You never check it.
# You repeat this with the remaining half.
# The catch: The list MUST be sorted first. You can't use this on a messy pile of books.

# 2. The Math (Logarithmic Time)
# If you have 1,000,000 items:
# Linear Search: Worst case = 1,000,000 guesses.
# Binary Search: Only 20 guesses. (Because you cut 1 million in half only 20 times before you get to 1).

# 3. The Algorithm Logic
# We use three pointers (indices):
# low (The start of the search zone)
# high (The end of the search zone)
# mid (The middle index)

# Pseudo-code logic
# while low <= high:
#     mid = (low + high) // 2  # Find middle index

#     if guess == target:
#         found it!
#     elif guess < target:
#         # Target is in the right half
#         low = mid + 1
#     else:
#         # Target is in the left half
#         high = mid - 1


# 🏋️ Coding Challenge: The Speed Demon
# I want you to implement the Binary Search. This is a classic interview question.
# The Task:
# Define binary_search(arr, target).
# Initialize low = 0 and high = len(arr) - 1.
# Write a while loop that runs as long as low <= high.
# Inside:
# Calculate mid using integer division //.
# Check if arr[mid] is the target. If yes, return mid.
# If arr[mid] is smaller than target, move low up (mid + 1).
# If arr[mid] is bigger than target, move high down (mid - 1).
# Return -1 if the loop finishes without finding it.

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


my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(my_list, 13))  # prints 6 (index of 13)
