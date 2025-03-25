import os

FILE_NAME = "calculations.txt"

def save_to_file(data):
    with open(FILE_NAME, "a") as file:
        file.write(data + "\n")

def read_from_file():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return file.readlines()
    return []

def calculator():
    print("Choose an operation: +, -, *, /")
    operation = input("Enter operator: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else "Error (Division by Zero)"
    }

    result = operations.get(operation, "Invalid operation")
    print(f"Result: {result}")

    # Save input and result
    data = f"{num1} {operation} {num2} = {result}"
    save_to_file(data)

    # Display stored calculations
    print("\nStored Calculations:")
    for line in read_from_file():
        print(line.strip())

calculator()
