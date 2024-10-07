class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")


student1 = Student("Aakash", 18)
student2 = Student("Geethika", 17)
student3 = Student("Chikku", 19)


student1.display_info()
student2.display_info()
student3.display_info()
