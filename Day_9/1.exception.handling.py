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
