# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create object of Dog
d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # From Dog
