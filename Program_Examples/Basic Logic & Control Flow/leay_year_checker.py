# Write a program that asks the user for a year and prints whether it is a leap year or not.
#  (Hint: Remember the rules for years divisible by 100 and 400!)

def check_leap(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap"
            else:
                return "Not Leap"
        else:
            return "Leap"
    else:
        return "Not Leap!"


year = int(input("Enter year to check: "))
x = check_leap(year)
print(x)
