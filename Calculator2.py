import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def square_root(x):
    return math.sqrt(x)

def exponentiation(x, y):
    return x ** y

def trigonometric_functions(angle, function):
    angle_rad = math.radians(angle)
    if function == 'sin':
        return math.sin(angle_rad)
    elif function == 'cos':
        return math.cos(angle_rad)
    elif function == 'tan':
        return math.tan(angle_rad)
    else:
        return "Invalid function"

def main():
    print("Simple Scientific Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (√)")
    print("6. Exponentiation (^)")
    print("7. Trigonometric Functions (sin, cos, tan)")

    choice = input("Enter the operation number or function: ")

    if choice in ['1', '2', '3', '4', '6']:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))

        if choice == '1':
            result = add(x, y)
        elif choice == '2':
            result = subtract(x, y)
        elif choice == '3':
            result = multiply(x, y)
        elif choice == '4':
            result = divide(x, y)
        elif choice == '6':
            result = exponentiation(x, y)

        print(f"Result: {result}")

    elif choice == '5':
        x = float(input("Enter the number: "))
        result = square_root(x)
        print(f"Result: {result}")

    elif choice == '7':
        angle = float(input("Enter the angle in degrees: "))
        trig_function = input("Enter the trigonometric function (sin, cos, tan): ")
        result = trigonometric_functions(angle, trig_function)
        print(f"Result: {result}")

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
