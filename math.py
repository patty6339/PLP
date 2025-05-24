# Get the first number
num1 = float(input("Enter first number: "))

# Get the operator
operator = input("Enter operator (+, -, *, /): ")

# Get the second number
num2 = float(input("Enter second number: "))

# Calculate and display result
if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Error: Invalid operator!")
