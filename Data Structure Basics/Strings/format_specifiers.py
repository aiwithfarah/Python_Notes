# format specifiers: {value:flag} --> formats a value based on flag inserted

price = 3000.14159

# 2 stands for the numbers after the floating point and f specifies floats
print(f"Price 1 is {price:.2f}")  # Price 1 is 3000.14
print(f"Price 1 is {price:,}")  # Price 1 is 3,000.14159
