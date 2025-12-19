# We use a structure called try and except to build a "safety net."
# try: "Attempt to run this dangerous code."
# except: "If the code above crashes, DO NOT stop. Jump here instead and handle it gracefully."

# TASK
# Create a variable stock = 100.
# Use input() to ask the user: "How much do you want to buy? " (Save this as user_input).
# Create a try / except block.
# Inside try:
# Convert user_input to an integer.
# Subtract that amount from stock.
# Print the new remaining stock.
# Inside except:
# Print "Invalid input! Please enter a number."


stock = 100
user_input = input("Ho much do you want to buy?: ")

try:
    user_input = int(user_input)
    stock -= user_input
    print(f"Remaining Stock: {stock}")
except ValueError:
    print("Invalid input. Please enter a number: ")
