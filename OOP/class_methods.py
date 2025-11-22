class Student:

    #  class variable count to count the number of students we create
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance Method
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    # class method
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_total_gpa(cls):
        return f"The total GPA is {cls.total_gpa}"


student1 = Student("farah", 3.14)
student2 = Student("rusu", 3.18)
print(Student.get_count())
print(Student.get_total_gpa())

# Total number of students: 2
# The total GPA is 6.32
