print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    result = a + b
    print("Result:", result)

elif choice == 2:
    result = a - b
    print("Result:", result)

elif choice == 3:
    result = a * b
    print("Result:", result)

elif choice == 4:
    if b != 0:
        result = a / b
        print("Result:", result)
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid choice.")
