# Count Up Timer

import time


def count(end, start=0):  # default args should be placed after positional args
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")


xx = count(10)
print(xx)
