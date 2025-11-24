# perform multiple tasks concurrently

import threading
import time


def walk_dog(first):
    time.sleep(8)  # walking the dog takes 8 seconds
    print(f"You finished walking {first}")


def take_outTrash():
    time.sleep(2)
    print("You take out the trash")


def get_mail():
    time.sleep(4)
    print("You get the mail")


# --> To add values for arguments we take one more argument args and pass the values as tuple
chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
chore1.start()

chore2 = threading.Thread(target=take_outTrash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")
# You take out the trash --> task that takes the shortest amount of time gets eecuted first, and concurretly other tasks are executing as well
# You get the mail
# You finished walking the dog
