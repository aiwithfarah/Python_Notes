# Challenge 1: The Blueprint
# Define a class called Student.
# Inside, write the __init__ method that accepts self, name, and score.
# Store those variables using self.name = name and self.score = score.

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def check_pass(self):
        if self.score > 40:
            print("Passed")
        else:
            print("Filed")
# Challenge 2: The Instance
# Create an object called student1 from your class. Pass in the name "Rahul" and score 95.
# Print student1.name


student1 = Student("Rahul", 95)
print(student1.name)  # Rahul

# Challenge 3: The Method
# Add a new method to your class called check_pass().
# Inside it, use an if statement:
# If self.score is greater than 40, print "Passed".
# Else, print "Failed".
# Call student1.check_pass().

student1.check_pass()  # Passed
