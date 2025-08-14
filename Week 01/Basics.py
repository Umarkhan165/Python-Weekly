# Problem 01: Add two numbers & also use input
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter the number 2:"))
Sum = num1+num2
print("The sum is :", Sum)

#Problem 02: Check The type of Variable Assigned
a = 8
print(type(a))
b = "8"
print(type(b))

# Problem 03 : Use comparison Opertaor 
n1 = 34
n2 = 80
print("n1 > n2", n1> n2)
print("n2 > n1", n2>n1)
print("n1 = n2", n1==n2)
# Problem 04: Remainder 
f = int(input("Enter value of a: "))
g = int(input("Enter value of b: "))
print("The remainder when a is divided by b is:", f % g)

# Problem 05: Average of two number:
avg = (n1+n2)/2
print("Avergae: ",avg)

# Problem 06: Sqaure of Numbers
sq = n1*n2
print("Square is :")
print(sq)

# Problem 07: Swap Two Numbers (without using a third variable)
h = 1
i = 2
h,i = i,h
print(h,i)
# Problem 08: Convert Celsius To Farehnite
C = int(input("Enter Temprature in Celcius:"))
F = (C * 9/5) + 32
print("The temprature in Farehnite is :", F)

# Problem 09: Check if Age is Eligible for Voting (>=18)
age = int(input("Enter you age: "))
print("ELigible" ,age>=18)
print("Not Eligible", age<18)
#  Problem 10: Find the Last Digit of a Number
number = int(input("Enter the number to find the last three digits: "))
last_digit = num % 10
print( "The last digit is : ", last_digit)




