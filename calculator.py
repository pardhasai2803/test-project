def add(a: float, b: float) -> float:
    """
    This function performs addition of two floating point numbers.

    Args:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of two numbers.

    Time Complexity:
    O(1) - Constant time complexity because it involves only one arithmetic operation.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    This function performs subtraction of two floating point numbers.

    Args:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The result of the subtraction.

    Time Complexity:
    O(1) - Constant time complexity because it involves only one arithmetic operation.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    This function performs multiplication of two floating point numbers.

    Args:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The product of two numbers.

    Time Complexity:
    O(1) - Constant time complexity because it involves only one arithmetic operation.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    This function performs division of two floating point numbers.

    Args:
    a (float): The dividend.
    b (float): The divisor.

    Returns:
    float: The quotient of two numbers.

    Raises:
    ValueError: If the divisor is zero or if the two numbers cannot be divided.

    Time Complexity:
    O(1) - Constant time complexity because it involves only one arithmetic operation,
           except in case of division by zero where it raises an error to indicate the invalid operation.
    """
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return a / b

def main():
    """
    This function serves as the main entry point of the calculator program.
    """
    while True:
        print("Calculator Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4', '5']:
            if choice == '5':
                break
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == '4':
                    try:
                        print(f"Result: {divide(num1, num2)}")
                    except ValueError as e:
                        print(str(e))
            except ValueError as e:
                print(str(e))
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()