# The Challenge: "The VIP List"You have a list of user names, but some are empty strings "" (ghost users).
# Filter out the empty strings.
# Map the remaining names to be Title Case(e.g., "alice" $\rightarrow$ "Alice").
# Output of the filer becomes the input of the map

users = ["alice", "", "bob", "charlie", "", "dave"]

vip_list = list(map(lambda x: x.title(), filter(lambda x: x != "", users)))

print(vip_list)
