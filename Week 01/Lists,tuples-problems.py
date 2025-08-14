# Problem # 1:
# Create a list of your favorite fruits and print them one by one
fruits = ["banana","mango","Pineapple"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Start with ["milk", "bread", "butter"] and replace "bread" with "eggs"

ab=["milk", "bread", "butter"]
fruits.pop(2)
fruits.insert(2,"eggs")
print(fruits)
# Start with an empty list and let the user add 3 products to it.
# Start with an empty cart
cart = []

# Loop 3 times to add products
for i in range(3):
    item = input(f"Enter product {i+1}: ")
    cart.append(item)

# Display final cart
print("\n Your shopping cart contains:")
for product in cart:
    print("-", product)



# Remove an Out-of-Stock Item
# From the list ["laptop", "mouse", "keyboard"], remove "mouse".

list_cart = ["laptop", "mouse", "keyboard"]
i = int(input("Enter number of item to remove: "))
list_cart.pop({i+1})




# Remove an Out of stock item:
ls= ["laptop", "mouse", "keyboard"]
ls.pop(1)
print(ls)

# Given [55, 89, 76, 45, 92], sort them in ascending order.

list = [55, 89, 76, 45, 92]
list.sort()
print(list)

# Given a list of movies, print only the first 3.
movies = ["Jumanji","3 idiots","Pi","Khan","New"]
for i in movies[:3]:
    print(i)

# Reverse a List
# Reverse ["red", "green", "blue", "yellow"] without using .reverse().

list = ["red", "green", "blue", "yellow"]
list.reverse()
print(list)

# Given [4, 9, 1, 17, 11], find the largest number manually (without max()).

numbers = [4, 9, 1, 17, 11]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)

