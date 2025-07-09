# 1
num = int(input("Enter a number to print its multiplication table:"))

for i in range(1,11):
    print (num, "x",i, "=",num*i)

# 2
correct_password = "Python123"

while True:
    password = input("Enter your password: ")
    if password == correct_password:
        print("✅ Access Granted.")
        break 
    else:
        print("❌ Incorrect password. Try again.")