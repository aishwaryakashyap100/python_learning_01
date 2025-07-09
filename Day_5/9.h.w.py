#task 1
def greet_user(name):
    print("Hello", name + "! Welcome to Python learning.")

greet_user("Aishwarya")


#task 2 
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

result = find_max(10, 25)
print("Maximum number is:", result)


#task 3
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "❌ Cannot divide by zero"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))


#task 4
def square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

sq, cu = square_and_cube(5)
print("Square:", sq)
print("Cube:", cu)


#task 5
def calculate_bill(bill_amount):
    if bill_amount >= 1000:
        discount = bill_amount * 0.10
    else:
        discount = 0

    final_amount = bill_amount - discount
    thank_you = "Thank you for shopping with us!"
    return discount, final_amount, thank_you

bill = float(input("Enter your bill amount: ₹"))
disc, total, message = calculate_bill(bill)

print("Discount Applied: ₹", disc)
print("Final Amount: ₹", total)
print(message)