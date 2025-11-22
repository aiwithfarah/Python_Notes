from class_def import Student

# creating an object
student1 = Student("farah", 33)

print(student1.age)  # 33
print(student1.name)  # farah
student2 = Student("Rusu", 6)
print(student2.name)  # Rusu
print(student2.age)  # 6

# Accessing methods
student1.eats()  # farah eats
