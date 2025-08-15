# What is a dictionary :
# A dictionary is a collection of key-value pairs.
# Each key is unique, and it maps to a value.

# Syntax 
student = {
    "name": "Umar",
    "age": 20,
    "course": "Python"
}

# Why use Dictionaries:
# Fast lookup → instead of searching a list, you can get values directly by key.
# Great for structured data (like user profiles, product info, settings)


# 4. When are they used in real life?
# Contact book → Name → Phone number
# Website user data → Username → Details
# Game inventory → Item → Quantity
# API responses (JSON) are basically dictionaries

my_dict = {
    "Brand":"Toyota",
    "model":"Corolla",
    "year":2020
}

print(my_dict["Brand"])
print(my_dict["model"])
print(my_dict["year"])

# Changing Values:
my_dict["year"]= 2021
print(my_dict["year"])

# Adding new pairs 
my_dict["color"]="Black"
print(my_dict["color"])

my_dict.pop("model")   # Removes by key
del my_dict["year"]    # Also removes
my_dict.clear()        # Clears all

# Looping through a Dictionary
for key, value in my_dict.items():
    print(key, ":", value)

# Nested Dictionaries:
students = {
    "student1": {"name": "Umar", "age": 20},
    "student2": {"name": "Ali", "age": 21}
}
print(students["student1"]["name"]) 
print(students["student2"]["name"])


# Contact Book using Dictionary
contacts = {
    "Umar": "1234567890",
    "Ali": "0987654321"
}

name = input("Enter name: ")
if name in contacts:
    print(f"{name}'s number is {contacts[name]}")
else:
    print("Contact not found!")
 