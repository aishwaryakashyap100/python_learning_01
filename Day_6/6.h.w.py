# 1
# Step 1: Create list
movies = ["Inception", "Interstellar", "The Matrix", "Titanic", "Avengers"]

# Step 2: Add a movie
movies.append("The Dark Knight")  # .append() adds to end

# Step 3: Remove a movie
movies.remove("Titanic")  # .remove() deletes by value

# Step 4: Print updated list
print("My Favorite Movies:", movies)

#2
# Step 1: Create tuple
person = (166, 44)  # (height in cm, weight in kg)

# Step 2: Access and print
print("Height:", person[0], "cm")
print("Weight:", person[1], "kg")

#3
# Step 1: Create set
hobbies = {"Reading", "Swimming", "Gaming"}

# Step 2: Add a new hobby
hobbies.add("Coding")  # .add() adds new element

# Step 3: Remove a hobby
hobbies.remove("Swimming")  # .remove() deletes item

# Step 4: Print
print("My Hobbies:", hobbies)

#4
# Step 1: Create dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "available": True
}

# Step 2: Print each
print("Title:", book["title"])
print("Author:", book["author"])
print("Available:", book["available"])

#5
# Step 1: Create dictionary
students = {
    "John": [85, 90, 95],
    "Sara": [78, 82, 88],
    "Mike": [92, 89, 84]
}

# Step 2: Loop through and calculate averages
for name, marks in students.items():
    average = sum(marks) / len(marks)
    print(f"{name}'s average marks: {average:.2f}")

