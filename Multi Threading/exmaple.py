import threading
import time


def eat_breafkast(name):
    time.sleep(2)  # simulating time taken to eat
    print(f"{name} eats breakfast!😑")


def drink_coffee(first_name, last_name):
    time.sleep(3)
    print(f"{first_name} {last_name} drinks coffee!☺")


# --With Threading--
start = time.time()

# Create thread objects
t1 = threading.Thread(target=eat_breafkast, args=("Farah",))
t2 = threading.Thread(target=drink_coffee, args=("Farah", "R"))

# start the threads. The run in the background
t1.start()
t2.start()

# .join() wait for them to finish, before printing the final time
t1.join()
t2.join()

end = time.time()
print(f"Finished in {end - start:.2f} seconds")

# Farah eats breakfast!😑
# Farah R drinks coffee!☺
# Finished in 3.0026767253875732 seconds
