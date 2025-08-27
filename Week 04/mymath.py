# mymath.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def format_contact(name, number):
    return f"{name}: {number}"

def is_valid_number(number):
    return number.isdigit() and len(number) == 10
