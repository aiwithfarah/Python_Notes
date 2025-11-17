import time

# time.sleep(3)
# print("Times up!!")  # will be printed after 3 seconds

my_time = int(input("Enter time in seconds: "))

for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)
print("Times Up!!!")

for x in range(my_time, 0, -1):
    seconds = x % 60
    print(f"00:00:{seconds}")
    time.sleep(1)
print("Times Up!")

# 00:00:5
# 00:00:4
# 00:00:3
# 00:00:2
# 00:00:1
# Times Up!
