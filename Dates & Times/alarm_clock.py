import time
import datetime  # allows us to work with sting representation of time
import pygame  # for sound effects (terminal pip install pygame)


def set_alarm(alarm_time):
    # alarm time is goin to be a string representation of time
    print(f"Alarm set for {alarm_time}")
    sound_file = "Dates & Times/my_music.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake Up ☺")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)


if __name__ == '__main__':
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

# To suppress"Hello from the pygame community. https://www.pygame.org/contribute.html:
# venv -lib - pygame - __init__ - scroll to the bottom find (if pygame_hide_support_prompt)
