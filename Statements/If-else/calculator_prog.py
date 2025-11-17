# Python calculator

operator = input("Enter an operator : '+ - / *' : ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == '/':
    print(num1 / num2)

elif operator == "*":
    print(num1 * num2)

else:
    print("Please select an operator from the given list")
