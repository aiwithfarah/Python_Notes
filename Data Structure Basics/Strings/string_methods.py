name = input("Enter your name: ")
result = len(name)
print(result)  # 5

print(name.find("r"))  # farah -->2 returns index of first occurence
# refres to reverse find #3. if pythn isn't able to locate a char it returns 0
print(name.rfind("a"))

name = name.capitalize()
print(name)  # Farah
print(name.upper())  # FARAH
print(name.lower())  # farah

print(name.isdigit())  # False
new_name = "7342a"
print(new_name.isdigit())  # False --> all need to be numbers
print(new_name.isalpha())  # False

phone_num = "123--456-789"
print(phone_num.count("-"))  # 3
print(phone_num.replace("-", "*"))  # 123**456*789
