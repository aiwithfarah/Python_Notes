unit = input("Is this temp in Celcius or Fahrenheit?: (C/F) ").lower()
temp = float(input("Enter the Temperature: "))

if unit == 'c':
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"Temp in Fahrenheit is : {temp}F")
elif unit == 'f':
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"Temp in Celcius is : {temp}C")
else:
    print("Invalid unit of measurement!")
