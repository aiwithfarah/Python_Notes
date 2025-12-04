# We want to measure how long a function takes to run.
# Instead of writing timer code inside every function, we write one decorator.
import time

# 1 The decorator (the wrapper factory)


def time_decoraor(func):

    # 2. The Warpper. The actual wrapping paper
    def wrapper():
        print("----Start Time----")
        start = time.time()

        func()  # --> Run the original function here

        end = time.time()
        print(f"----Finished in {end-start:.2f} seconds----")
    return wrapper

# 3. Using it


@time_decoraor
def heavy_calculation():
    time.sleep(1)  # sleep for 1 sec
    print("Calculation is Done!")


# 4. Run it
# We call the func normally, but the decorator logic runs automatically!
heavy_calculation()
