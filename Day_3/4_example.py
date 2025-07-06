# Asking user for total bill amount
bill_amount = float(input("Enter your total bill amount: "))

# Deciding discount based on amount
if bill_amount >= 1000:
    discount = bill_amount * 0.20        # 20% discount
elif bill_amount >= 500:
    discount = bill_amount * 0.10        # 10% discount
else:
    discount = 0                         # No discount

# Calculating final amount after discount
final_amount = bill_amount - discount

# Displaying the results
print("Your discount is:", discount)
print("Amount to pay:", final_amount)
