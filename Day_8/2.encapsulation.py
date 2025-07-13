class BankAccount:
    def __init__(self):
        self.__balance = 0    # Private variable (double underscore)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(1000)
print("Balance:", acc.get_balance())  # ✅ Okay

# print(acc.__balance)               ❌ Error: private variable