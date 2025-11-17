# A = P(1 + r/n)t
# A = Final Amount
# P = Initial Principle Balnce
# r = interest rate
# t = number of time

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter principle amount: "))
    if principle <= 0:
        print("Principle amount can't be less than or equal to 0")

print(principle)

while rate <= 0:
    rate = float(input("Enter interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to 0")

print(rate)

while time <= 0:
    time = float(input("Enter time: "))
    if time <= 0:
        print("Time can't be less than or equal to 0")

print(principle)

total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} years : {total:.2f}")
