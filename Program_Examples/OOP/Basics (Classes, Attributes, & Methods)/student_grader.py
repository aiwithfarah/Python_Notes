# 2. The Student Grader

# Goal: Create a class called Student.

# Attributes: name, score.

# Methods: Create a method called check_pass() that checks the score.

# If score >= 50, return "Passed".

# If score < 50, return "Failed".

# Test: Create a student with score 40 and one with 90. Check their results.

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def check_pass(self):

        if self.score >= 50:
            return "Passed"
        else:
            return "Failed"


student1 = Student('Farah', 40)
student2 = Student('Rusu', 90)

print(student1.check_pass())  # Failed
print(student2.check_pass())  # Passed
