import math

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.
    """
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

def circle_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius ** 2  # correct formula

def get_first_char(text):
    """
    Get the first character of a text.

    Args:
        text (str): The text.

    Returns:
        str or None: The first character of the text, or None if the text is empty.
    """
    if len(text) == 0:
        return None
    return text[0]

def countdown(n):
    """
    Print a countdown from n to 1.

    Args:
        n (int): The number to start the countdown from.
    """
    while n > 0:  
        print(n)
        n -= 1  

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    return (celsius * 9 / 5) + 32  # correct formula

# Main
print(calculate_average([1, 2, 3]))
print(circle_area(5))
print(get_first_char("hello"))
countdown(4)
print(celsius_to_fahrenheit(100))