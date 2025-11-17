import random

low = 1
high = 100
num = random.randint(low, high)  # for whole numbers
print(num)

number = random.random()
print(number)

options = ("rok", "paper", "scissors")
random_choice = random.choice(options)
print(random_choice)


cards = [1, 2, 3, 4, 5, 6]
random.shuffle(cards)
print(cards)
