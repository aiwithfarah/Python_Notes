# Used to chain conditionals and or not

temp = 25
is_raining = False

if temp > 40 or temp < 0 or is_raining == True:  # atleast one condition needs to evaluate o true
    print("Cancel the outdoor event!")
else:
    print("Outdoor event is on!")

# Outdoor event is on!

new_temp = 25
is_sunny = True

if temp >= 28 and is_sunny:  # both conditions need to evaluate to true
    print("It is hot outside!")
else:
    print("It s pleasant outside!")

# It s pleasant outside!

temp = 25
is_sunny = True

if temp < 28 and not is_sunny:  # inverses the condition
    print("It's kind of cold!")
