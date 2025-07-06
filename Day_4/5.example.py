balance = 5000                           # Initial bank balance

while True:
    amount = int(input("Enter amount to withdraw: "))
    
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print("Withdrawal successful.")
        print("Remaining balance:", balance)
    
    choice = input("Do you want another transaction? (yes/no): ")
    if choice.lower() != "yes":
        break                            # Exit the loop if user says no
