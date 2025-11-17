# Python weight convertor kg/pounds

weight = float(input("Enter your weight: "))
unit = input("Is this weight in K(lg) or L(POUNDS)?: ").lower()

if unit == 'k':
    weight *= 2.205
    unit = "Lbs"
elif unit == 'l':
    weight /= 2.205
    unit = "Kgs"
else:
    print("Incorrect input: ")

print(f"Your weight is {round(weight, 2)} in {unit}")
# Your weight is 81.63 in Kgs
