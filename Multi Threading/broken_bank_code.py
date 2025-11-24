import threading

balance = 0  # gloal variable
lock = threading.Lock()  # create the lock

# def deposit():
#     global balance
#     for _ in range(10000):
#         balance += 1


def deposit():
    global balance

    for _ in range(1000):
        # Lock the door
        lock.acquire()

        # Do the sensitive work
        balance += 1

        # unlock the door
        lock.release()


# create 2 threads
t1 = threading.Thread(target=deposit)
t2 = threading.Thread(target=deposit)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Final Balance: {balance}")
