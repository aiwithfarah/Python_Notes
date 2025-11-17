import math
x = 2
y = 9.6
pi = math.pi
print(pi)  # 3.141592653589793
sqrt = math.sqrt(4)  # -- Returns square root f a number
print(sqrt)  # 2.0
print(math.ceil(y))  # 10 -- rounds a value up to the nearet number
print(math.floor(y))  # 9 -- rounds a value down to the nearest number


# caluculate circumference of a circle - 2*pi*r

radius = float(input("Enter the radius : "))
circumference = 2 * math.pi * radius
print(f"{round(circumference, 2)}")  # rounds to 2 digits
# 65.97

# calcuate area of a cricle pi*r2

radius = float(input("Enter the radius ifthe circle : "))
area = math.pi * pow(radius, 2)
print(f"Area of the circle is {round(area, 2)}cm^2")
# Area of the circle is 346.36cm^2

# find hypotenuese of a right triangle c = sqrt(a2 + b2)

sideA = float(input("Enter length of side A: "))
sideB = float(input("Enter length of side B: "))
hypotenuese = math.sqrt(pow(sideA, 2) + pow(sideB, 2))
print(f"Site C = {hypotenuese}")  # 5.0
