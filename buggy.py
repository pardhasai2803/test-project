import math

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

def circle_area(radius):
    return math.pi * radius ** 2  # correct formula

def get_first_char(text):
    if len(text) == 0:
        return None
    return text[0]

def countdown(n):
    while n > 0:  
        print(n)
        n -= 1  

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32  # correct formula

# Main
print(calculate_average([1, 2, 3]))
print(circle_area(5))
print(get_first_char("hello"))
countdown(4)
print(celsius_to_fahrenheit(100))