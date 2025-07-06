apple_price = float(input("Enter price of one apple: "))
apple_qty = int(input("Enter quantity of apples: "))
banana_price = float(input("Enter price of one banana: "))
banana_qty = int(input("Enter quantity of bananas: "))
apple_total = apple_price * apple_qty
banana_total = banana_price * banana_qty
total_bill = apple_total + banana_total
print("Your total grocery bill is:", total_bill)