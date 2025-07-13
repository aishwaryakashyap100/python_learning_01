# 1
# Parent class
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

# Child class 1
class Car(Vehicle):
    def start(self):
        print("🚗 Car is starting with key ignition.")

# Child class 2
class Bike(Vehicle):
    def start(self):
        print("🏍️ Bike is starting with self-start button.")

# Testing the classes
v = Vehicle()
v.start()

c = Car()
c.start()

b = Bike()
b.start()
#2
class LoginSystem:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private variable using double underscore

    def login(self, entered_username, entered_password):
        # Check if both username and password match
        if self.username == entered_username and self.__password == entered_password:
            print(f"✅ Welcome, {self.username}! Login successful.")
        else:
            print("❌ Invalid username or password.")

# Testing Login System
user1 = LoginSystem("admin", "secret123")
user1.login("admin", "secret123")      # ✅ Correct
user1.login("admin", "wrongpassword")  # ❌ Wrong
#3
from abc import ABC, abstractmethod

# Abstract base class
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete class 1
class CardPayment(Payment):
    def pay(self, amount):
        print(f"💳 Paying ₹{amount} via Credit/Debit Card.")

# Concrete class 2
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"📱 Paying ₹{amount} via UPI.")

# Testing
card = CardPayment()
card.pay(1500)

upi = UPIPayment()
upi.pay(800)
#4
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Polymorphism in action
shapes = [Square(4), Rectangle(5, 3)]

for s in shapes:
    print(f"Area: {s.area()}")
