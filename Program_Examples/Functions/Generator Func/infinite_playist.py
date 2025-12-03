# Your Task: Write a generator function called infinite_repeat(word) that takes a word and yields it forever.

def infinite_repeat(song):

    while True:

        yield song


playist = infinite_repeat("Song A")
print(next(playist))
print(next(playist))

# Song A
# Song A
