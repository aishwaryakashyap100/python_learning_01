# Asking for user's age
age = int(input("Enter your age: "))

# Asking if user has a ticket (Yes/No as text)
ticket_input = input("Do you have a ticket? (yes/no): ")

# Converting ticket input to Boolean
has_ticket = ticket_input.lower() == "yes"

# Decision using comparison + logical operator
if age >= 18 and has_ticket:
    print("You can watch the movie!")
else:
    print("Sorry, you cannot watch the movie.")
    