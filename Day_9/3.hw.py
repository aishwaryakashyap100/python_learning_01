#1
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("❌ Cannot divide by zero!")

except ValueError:
    print("❌ Please enter only numbers!")

else:
    print("✅ Division successful.")

finally:
    print("✅ This block always runs (used for cleanup).")
#2
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("🚫 You must be 18 or older to enter.")
else:
    print("✅ Access granted.")
#3
# Task: Open and read a file, handling missing file or permission issues

try:

    file = open("data.txt", "r")
    content = file.read() 
    print("✅ File Content:\n", content)
    file.close()

except FileNotFoundError:
    print("❌ File not found. Please check the filename or path.")

except PermissionError:
    print("❌ You don't have permission to access this file.")

finally:
    print("✅ File handling task completed (finally block).")
#4

def login_system():
    correct_username = "admin"
    correct_password = "1234"

    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if not isinstance(username, str) or not isinstance(password, str):
            raise TypeError("❌ Invalid data type entered. Must be text.")

        if username == correct_username and password == correct_password:
            print(f"✅ Welcome {username}! You have successfully logged in.")
        else:
            print("❌ Incorrect username or password.")

    except TypeError as e:
        print("⚠️ Error:", e)

    except Exception as e:
        print("⚠️ Something unexpected went wrong:", e)

    finally:
        print("🔒 Login process ended (finally block).")

login_system()