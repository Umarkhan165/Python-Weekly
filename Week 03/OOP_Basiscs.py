# Problem 01:
# Class Created
class car:
    def __init__(self, brand , color):
        self.brand= brand
        self.color=color

    def drive(self):
        print(f"{self.color} {self.brand} is driving..")
# Objects 
car1 = car("Toyota","Black")
car2 = car("BMW","Red")

# Methdos
car1.drive()
car2.drive()

# Problem 02:
# Student Class
# Create a class Student with attributes: name, age, grade
# Add a method introduce() that prints "Hi, I am Umar, I am 20 years old, and my grade is A."

class Car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    def drive(self):
        print(f"The {self.color} {self.brand} {self.model} is driving...")
car1 = Car("Toyota", "Red", "Corolla")
car2 = Car("Honda", "Blue", "Civic")


car1.drive()
car2.drive()

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"Hi, I am {self.name}, I am {self.age} years old, and my grade is {self.grade}.")

student1 = Student("Umar", 20, "A")
student1.introduce()

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

# Example usage
calc = Calculator()
print("Add:", calc.add(10, 5))
print("Subtract:", calc.subtract(10, 5))
print("Multiply:", calc.multiply(10, 5))
print("Divide:", calc.divide(10, 5))
