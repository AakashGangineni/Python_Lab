class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Aakash", 18)
person2 = Person("Geethika", 17)


print(f"Person 1: Name: {person1.name}, Age: {person1.age}")
print(f"Person 2: Name: {person2.name}, Age: {person2.age}")
