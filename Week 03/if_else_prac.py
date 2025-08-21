x = input('ENter you name: ')
if x=="Khan":
    print("This is your name: ", x)
elif x=="Umar":
    print("the name is wrong")
else:
    print('This is not your name')


# Lists and Tuples Practice :
y = [1,True,"hi"]
print(len(y))
print(y)
y.extend([2,3,3,4,4])
print(y)
print(y.pop(1))
print(y)
# Change its value of the list also i can do That;
y[0]=3
print(y)

# Tuple is a list without the square [] bracket 
# Tuple is made of round bracktes and also it is immutable or we can say unchangeable

x = (1,2,23,4,5)
print(x)


# For Loops :

for i in range(10):
    print(i)
for b in range(10, -1, -1 ):
    print(b)

# Loop for the [1,2,2,3,]
# Lists & Tuples
h = [23,3,5,5]
for i in range(len(x)):
    print(x[i])
    