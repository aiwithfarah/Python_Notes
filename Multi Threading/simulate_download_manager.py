# The Goal: Simulate a "Download Manager" that downloads 3 large files at the same time.

import threading
import time


def download_file(file_name, seconds):

    print(f"{file_name} started downloading...")
    time.sleep(seconds)
    print(f"{file_name} finished")


start = time.time()
# create threads
t1 = threading.Thread(target=download_file, args=("Movie.mp4", 4))
t2 = threading.Thread(target=download_file, args=("Song.mp3", 2))
t3 = threading.Thread(target=download_file, args=("Picture.png", 1))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("All downloads complete!")
end = time.time()
print(f"It took {end - start:.2f} seconds to download all the files!")
