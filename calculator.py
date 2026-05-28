def add(a: float, b: float) -> float:
    """
    This function calculates the sum of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    This function calculates the difference between two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference of a and b.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    This function calculates the product of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    This function calculates the quotient of two numbers.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient of a and b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b