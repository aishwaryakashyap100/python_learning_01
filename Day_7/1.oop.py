# Creating a class named Student
class Student:
    
    # Constructor method to initialize object attributes
    def __init__(self, name, age, marks):
        self.name = name            # Object's name
        self.age = age              # Object's age
        self.marks = marks          # Object's marks

    # Method to display student's details
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    # Method to check if the student passed
    def check_pass(self):
        if self.marks >= 33:
            print("Result: ✅ Pass")
        else:
            print("Result: ❌ Fail")

# Creating an object (student1) of the Student class
student1 = Student("Aishwarya", 21, 85)

# Calling methods on the object
student1.display_info()
student1.check_pass()