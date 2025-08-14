
# 1. What is a List?
# A list is a collection of items stored in a single variable.
# Items can be of any data type: numbers, strings, booleans, even other lists.
# Lists are ordered (items have positions) and mutable (can be changed).

# 2. How does a List work?
# A list is like a container (or basket) holding items.

# Each item has an index starting from 0.

# You can add, remove, or change items.

# 3. Why do we have Lists?
# Lists make it easy to store and manage multiple values without creating multiple variables.
#  we make lists like this :
student1 = "Umar"
studnet2 = "Khan"
#it can be created in teh same way:
students = ["Umar", "Khan"]


# When are Lists used in real life?
# E-commerce: Store items in a cart
# School system: Store student names
# Game: Store player scores
# Data analysis: Store large datasets for processing

print(students[0])
print(students[1])
# Indexing, modifying and negative indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
print(fruits[-2])
print(fruits[0:1])
print(fruits[0:3])
print(fruits)

#  Common methods of a list : 
fruits.append("orange")  # Add to end
fruits.insert(1, "grape") # Add at position
fruits.remove("apple")    # Remove by value
fruits.pop(2)             # Remove by index
fruits.sort()             # Sort list
fruits.reverse()          # Reverse order
print(fruits)

for i in fruits:
    print(i)

# What is a Tuple?
# Tuple is like a list but immutable (cannot be changed)
# Created with () instead of [].
# python
# Copy
# Edit
colors = ("red", "green", "blue")
print(colors[0])
#   It is immutable means unchangable when we do 
# colors[0] = "Yellow"
# There is a Error
# 12. Real Applications
# Lists: shopping carts, playlists, game inventory

# Tuples: storing fixed data like country codes, RGB color values
