def greet(name):
    return f"hello,{name}"

print(greet("umar"))

# Base Case → when to stop recursion.
# Recursive Case → function calls itself with smaller input

def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive case

print(factorial(5))  # 120


def square(x):
    return x*x

# Lambda funcitons 
# it is a one line function like other funtctions 
square = lambda x: x*x
print(square(5))
# Lists 
num = [1,2,3,4,5]
squares = list(map(lambda x: x*x , num))
print(squares)