import threading
import time


def download_file(file_name):

    print(f"Downloading {file_name}")
    time.sleep(2)  # simulating a ait
    print(f"Finished {file_name}")


# Create 2 threads
t1 = threading.Thread(target=download_file, args=("File_A",))
t2 = threading.Thread(target=download_file, args=("File_B",))

# Start them. They run simultaneously
t1.start()
t2.start()

# wait for them to finish
t1.join()
t2.join()
