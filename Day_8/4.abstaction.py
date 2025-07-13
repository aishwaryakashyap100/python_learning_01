from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print("Circle Area:", c.area())