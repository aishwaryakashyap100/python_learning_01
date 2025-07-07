# Function to calculate total bill with discount
def calculate_bill(amount):
    if amount >= 1000:
        discount = amount * 0.10
    else:
        discount = 0
    total = amount - discount
    return total, discount

# Taking user input
bill = float(input("Enter bill amount: "))
final_amount, discount = calculate_bill(bill)

print("Discount:", discount)
print("Total to pay:", final_amount)