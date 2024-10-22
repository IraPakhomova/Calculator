def add(a, b):
    return a + b

def subtract(a, b):
    return a-b

operation = input("Enter operation (+/-):")

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number: "))

if operation == '+':
    print(f"Result:{add(num1, num2)}")
elif operation == '-':
    print(f"Result: {subtract(num1, num2)}")
else:
    print("Unsupported operation. Use '+' or '-'.")