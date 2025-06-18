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

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    try:
        choice = int(input("Enter operation choice (1-4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice")
            return
        
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
    
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    calculator()
