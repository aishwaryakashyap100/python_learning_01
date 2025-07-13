# 1
class Product:
    def __init__(self, name, price, discount):
        self.name = name                    # Name of the product
        self.price = price                  # Original price
        self.discount = discount            # Discount in %

    def get_final_price(self):
        # Calculating price after discount
        final_price = self.price - (self.price * self.discount / 100)
        return final_price

# Creating a product
p = Product("Laptop", 50000, 10)
print("Product:", p.name)
print("Final Price after Discount:", p.get_final_price())
# 2
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0                      # Initial balance is 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("❌ Insufficient balance.")

    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")

# Usage
acc = BankAccount("Aishwarya")
acc.deposit(1000)
acc.withdraw(500)
acc.show_balance()
#3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True              # Book is available by default

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        self.is_available = True
        print(f"You have returned '{self.title}'.")

# Usage
b1 = Book("Python for Beginners", "John Doe")
b1.borrow()
b1.borrow()            # Already borrowed
b1.return_book()
b1.borrow()            # Borrow again after returning
# 4
class UserLoginSystem:
    def __init__(self, username, password):
        self.username = username
        self.__password = password           # Private password for security
        self.is_logged_in = False

    def login(self, entered_username, entered_password):
        if entered_username == self.username and entered_password == self.__password:
            self.is_logged_in = True
            print(f"✅ Welcome, {self.username}. You are now logged in.")
        else:
            print("❌ Invalid username or password.")

    def logout(self):
        if self.is_logged_in:
            self.is_logged_in = False
            print(f"👋 {self.username} has logged out.")
        else:
            print("⚠️ You are not logged in.")

# Usage
user = UserLoginSystem("admin", "1234")
user.login("admin", "1234")
user.logout()
user.logout()

