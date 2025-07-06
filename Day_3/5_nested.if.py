# Asking for age and membership status
age = int(input("Enter your age: "))
member = input("Are you a member? (yes/no): ")

# Outer condition
if age >= 18:
    # Inner condition
    if member.lower(18) == "yes":
        print("You get a special discount!")
    else:
        print("You can enter but no discount.")
else:
    print("Sorry, you're not eligible.")
