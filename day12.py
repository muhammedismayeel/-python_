class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

# Object creation OUTSIDE the class
student1 = Student("Ismayeel", 19, "A+")
student1.display_info()

        