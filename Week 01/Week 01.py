# Problem 01
# Store Your Info
# Create variables to store your name, age, and country. Print them in a sentence like:
# My name is Umar, I am 20 years old, and I live in Pakistan.
my_info = "My name is Umar, I am 20 years old, and I live in Pakistan"
print(my_info)

# Problem 02:
# Check Data Types
# Store:
# 5 in a variable
# "Python" in another
# True in another
# Print each variable’s type.

a = 5
b = "Python"
c = True

print(type(a))
print(type(b))
print(type(c))

# Problem 03:
h = 3.14
print(type(h))
print(int(3.14))
print(type(h))

# Problem 04:
# Store item price = 250 and quantity = 3. Calculate the total bill.
price = 250
quantity = 3
total = price * quantity
print("The Total is : ")
print(total)

# Problem 05:
# Store today’s temperature in Celsius and convert it to Fahrenheit.
C = int(input("Enter Temprature in Celcius:"))
F = (C * 9/5) + 32
print("The temprature in Farehnite is :", F)

# Problem 06
# Student Report
n= input("Name: ")
r = input("Rollno: ")
c = input("Class: ")
s = input("Section: ")
print("Name is : ",n)
print("Class is :",c)
print("Section is: ", s)

# Input/Output (I/O)?

num1 = input("Ente the numebr :")
num2 = input("Enter teh number 2: ")
print("Sum is : ", num1 + num2)
# Exmaples :
# Simple print
print("Hello World")

# Printing variables
name = "Umar"
print("My name is", name)

# Using f-strings (cleaner)
print(f"My name is {name}")


num1 = int(input("Enter the numebr :"))
num2 = int(input("Enter teh number 2: "))
print("Sum is : ", num1 + num2)



# Loops


# Printing numbers 1 to 5
for i in range(1, 6):
    print(i)
# Loop in which lis is used
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Count example
count = 1
while count <= 5:
    print(count)
    count += 1
# Continue Exmaple

while True:
    print("This will run forever unless you break it")
    break

# Real Life example:

real_pin = 1234
attempt = 0
while attempt < 5:
    pin=input("Enter you pin: ")
    if pin ==real_pin:
        print("Access Granted")
        break   
    else:
        print("Blocked")
    attempt +=1



