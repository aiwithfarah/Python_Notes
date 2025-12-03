# Most people think map only takes one list. But actually, map can handle as many lists as you want!

# When you pass two lists to map, it grabs the first item from List A and the first item from List B, and passes them both to your function at the same time.

# The Rules:

# Multiple Lists: You pass them as extra arguments: map(function, list1, list2).

# The Lambda: Your lambda function needs two arguments now (usually x and y).

# The Length: It stops automatically when the shortest list runs out of items.

#   The Challenge: "The Total Score" 🎮
# Imagine you are hosting a game tournament. You have the scores from Round 1 and Round 2 in separate lists.
# You need to calculate the Total Score for each player.

round_1 = [10, 20, 30]
round_2 = [5, 15, 25]

totals = list(map(lambda x, y: x+y, round_1, round_2))
print(totals)
