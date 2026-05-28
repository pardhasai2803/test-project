def add(a: float, b: float) -> float:
    """Returns the sum of two numbers.

    Args:
    a (float): First number.
    b (float): Second number.

    Returns:
    float: Sum of a and b.

    Example:
    >>> add(5, 7)
    12
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers.

    Args:
    a (float): First number.
    b (float): Second number.

    Returns:
    float: Difference of a and b.

    Example:
    >>> subtract(7, 5)
    2
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers.

    Args:
    a (float): First number.
    b (float): Second number.

    Returns:
    float: Product of a and b.

    Example:
    >>> multiply(5, 7)
    35.0
    """
    return a * b

def divide(a: float, b: float) -> float:
    """Returns the quotient of two numbers or raises ValueError if division by zero.

    Args:
    a (float): First number.
    b (float): Second number.

    Returns:
    float: Quotient of a and b.

    Raises:
    ValueError: If b is zero.

    Example:
    >>> divide(10, 2)
    5.0
    >>> divide(10, 0)
    ZeroDivisionError: Error: Division by zero is not allowed.
    """
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return a / b

def main():
    """Program to perform basic arithmetic operations."""
    print("Calculator Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
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
                print(f"Result: {divide(num1, num2)}")
        except ValueError as e:
            print(str(e))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()