#task 1
num = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


#task 2
correct_password = "Python123"

while True:
    password = input("Enter your password: ")
    if password == correct_password:
        print("✅ Access Granted.")
        break 
    else:
        print("❌ Incorrect password. Try again.")


#task 3
products = ["Apple", "Banana", "Avocado", "Grapes", "Apricot", "Mango"]

for item in products:
    if item.startswith("A"): 
        print(item)


#task 4
while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '4':
        print("Exiting calculator. Goodbye!")
        break 

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    else:
        print("Invalid choice. Please select between 1-4.")