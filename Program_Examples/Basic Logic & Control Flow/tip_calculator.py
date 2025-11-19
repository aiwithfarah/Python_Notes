# Create a function that takes a bill amount and a tip percentage (e.g., 15%) and returns the final total
# Ensure you handle inputs that aren't numbers gracefully.

def tip_calculator(amount, tip):

    final_total = 0

    if amount <= 0:
        print("Please enter a valid amount!")
    else:
        final_total = amount + (amount * (tip/100))

    return final_total


try:
    amount = float(input("Enter the total amount: "))
    tip = float(input("How much tip would you like to give?: "))
    x = tip_calculator(amount, tip)
    print(f"Total Amount including tip : {x}")
except ValueError:
    print("Please enter only numbers. Not Text")
