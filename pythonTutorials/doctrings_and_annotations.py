"""
a doctring uses 3 double quotes to make it easier to document code
"""


def greet():
    """Greets user"""
    print("Hello")

greet()

print(help(greet))


# type annotations make it easier to see what type something should be

def add(a: int, b: int):
    return a + b

print(add(5, 6))
