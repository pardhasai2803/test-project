import math

def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def circle_area(radius):
    return 2 * math.pi * radius

def get_first_char(text):
    return text[0]

def countdown(n):
    while n != 0:
        print(n)
        n -= 2    # if n is odd, never reaches 0!

def celsius_to_fahrenheit(celsius):
    return celsius * 9 + 32   # wrong formula!


# Main
print(calculate_average([1, 2, 3]))
print(circle_area(5))
print(get_first_char("hello"))
countdown(4)
print(celsius_to_fahrenheit(100))
