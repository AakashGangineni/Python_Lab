class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


student = Student("Aakash", 18)

print(f"Student Name: {student.name}, Roll Number: {student.roll_no}")
