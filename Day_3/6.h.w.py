#task 1
age = int(input("Enter your age: "))

if age < 12:
    print("You are a Child.")
elif age >= 13 and age <= 19:
    print("You are a Teenager.")
elif age >= 20 and age <= 59:
    print("You are an Adult.")
elif age >= 60:
    print("You are a Senior.")
else:
    print("Invalid age entered.")


 #task 2
correct_username = "admin"
correct_password = "123456" \

username = input("Enter your username:")
password = input("Enter your password:")

if username == correct_username and password == correct_password:
    print("Welcome,", username +"!Access Granted.")
else:
    print ("Access denied.Invalid username or password.")


#task 3
balance = float(input("Enter your current balance: ₹"))

withdrawal_amount = float(input("Enter amount to withdraw: ₹"))

if withdrawal_amount <= balance:
    balance -= withdrawal_amount 
    print("✅ Withdrawal successful!")
    print("Remaining balance: ₹", balance)
else:
    print("❌ Insufficient funds. Transaction denied.")
    print("Your available balance: ₹", balance)