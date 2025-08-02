# Simple calculator
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    result = None
    print("Invalid operator.")

# Print the calculation and result if the operator was valid
if result is not None:
    print(num1, op, num2, "=", result)
