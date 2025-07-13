class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

# Polymorphism in action
for animal in (Cat(), Dog()):
    animal.speak()   # Same method name ➔ different behavior