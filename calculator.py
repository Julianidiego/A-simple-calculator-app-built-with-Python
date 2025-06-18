def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of negative number"
    return x ** 0.5

def modulo(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x % y

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Modulo (Remainder)")
    
    try:
        choice = int(input("Enter operation choice (1-7): "))
        if choice not in range(1, 8):
            print("Invalid choice")
            return
        
        if choice == 6:  # Square root only needs one number
            num1 = float(input("Enter number: "))
            print(f"Square root of {num1} = {square_root(num1)}")
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == 1:
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 4:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == 5:
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == 7:
                print(f"{num1} % {num2} = {modulo(num1, num2)}")
    
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    calculator()
