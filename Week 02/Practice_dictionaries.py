student = {
    "name":"Umar",
    "class":"2nd"
}

print(student["class"])
student["class"]="3rd"
print(student["class"])

# Removing items
student.pop("name")
# print(student["name"])

# Looping through a Dictionary

for key in my_dict.items():
    print(key,":", value)


# Nested DIctionaries
students = {
    "Student1" :{"name":"Umar","age":21},
    "Student2": {"name":"ALi","age":22}
}
print(students["Student1"]["name"])

# Contact Book using DIctionaries
contact ={
    "Umar":"03014142178",
    "Khan":"179210280-1"
}
name = input("Enter your name here:")
if name in contact:
    print(f"{name}'s Number is {contact[name]}")
else:
    print("name is not in teh contact List")

# Problmes:


# Problem 01 :
# Store name, age, and grade of a student in a dictionary and print it.
dict_01 ={
    "Name":"Umar",
    "age":21,
    "grade":"b"
}
print(dict_01["Name"])
print(dict_01["age"])
print(dict_01["grade"])
# Access Dictionary Value
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print(car["model"])
# Add a New Key-Value Pair
car["color"] = "black"
print(car["color"])

# Update Value
# Change the "year" of the car dictionary to 2023.
car["year"] = 2030
# Remove "model" from the car dictionary.
car.pop("model")
# Clear all key values form the dictionaries
car.clear()
# Level 03- Looping:
fruit_prices = {"apple": 100, "banana": 60, "mango": 150}
for key in fruit_prices:
    print(key,"is",fruit_prices[key])
    
# Ask the user for a fruit name and print its price if it exists.
name_fr = input("Enter the name of fruit: ")
if name_fr in fruit_prices:
    print(fruit_prices[name_fr])
else:
    print("Name is not in teh list")

# Level 4 – Nested Dictionaries
students = {
    "student1": {"name": "Umar", "age": 20},
    "student2": {"name": "Ali", "age": 21}
}

print(students["student1"]["age"])