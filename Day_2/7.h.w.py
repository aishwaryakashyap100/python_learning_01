#task 1
number_1 = int(input("Enter number_1:"))
number_2 = int(input("Enter number_2:"))
print (number_1+number_2)
print (number_1-number_2)
print (number_1*number_2)
print (number_1/number_2)
print (number_1//number_2)
print (number_1%number_2)
print (number_1**number_2)


#task 2
age = int(input("Enter your age:"))
ID = input("You have id? (yes/no):")
if age>=18 and ID.lower() == "yes":
     print("Entry allowed")
else:
     print("Entry Denied")