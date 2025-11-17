questions = ("Elemnets in the Perodic Table?: ",
             "Which animal lays the largest eggs?: ", "Most abundant gas on Earth?: ",
             "How many bones are in a Human body?: ", "Hottest planet in Solar System? ")

options = (('A. 45', 'B 55', 'C 65', 'D 118'), ('A. Emu', 'B. Chicken', 'C. Ostrich', 'D. Bald Eagle'),
           ('A. Oxygen', 'B. Nitrogen', 'C. Helium',
            'D. Co2'), ('A. 345', 'B. 345', 'C. 255', 'D. 206'),
           ('A. Mercury', 'B. Jupiter', 'C. Venus', 'D. Earth'))

answers = ('D', 'C', 'D', 'D', 'C')
guesses = []
score = 0
question_num = 0


for question in questions:
    print("--------------------------------")
    print(question)
    # dispaly every option
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess:(A, B, C, D) ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print(f"Incorrect! {answers[question_num]} is the correct answer")
    question_num += 1

print('-----------------------------')
print("------Results----------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)

print(f"Your final score is {score}%")
