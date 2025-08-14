# Strings:

# What is a string: A string is a data type in pyhton it is used to store text using different metods "" ,'' , ''' ''' for multiline string.
# # Strings:

# What is a string: A string is a data type in pyhton it is used to store text using different metods "" ,'' , ''' ''' for multiline strings
# How does it work? :
# It stores the value of the each charcter or alphabet uniquely liek :"Umar" = ['U','m','a','r'] = [0,1,2,3,]
# What: Extracting part of a string.
# How: string[start:end] → end is excluded.
# Why: To get substrings.
# When: Parsing emails, URLs, file names.
print("Creating strings:")
name = "Umar"
quote = 'code with me '
paragraph = '''This is a multi line string 
ok 
then'''

print(name)
print("Indexing the strings")
print(name[0])
print(name[-1])
print(quote)
print(paragraph)
print("-------")
print("String Slicing")


text = "hello pyhton"
print(text[0:3])
print(text[0:])
print(text[5:])

# Real world use case is extarcting the parts of email addresses like or instagram id's etc 
# Example is :
gmail = "uzairyaqoob176@gmail.com"
names = "khan_umar"
print(gmail[0:5])
print(names[5:])

# Strings Methods
# String methdos are the built in funtions with strings
# It is used for data cleaning , formatting , and validaion
msg = "Python is a really fun langugage"
print(msg.strip())
print(msg.lower())
print(msg.upper())
print(msg.replace("fun", "Awesome"))
print("Real world use case:")
# During entering the data in a form we need to clean the data so:
puts = input("ENter you name :")
print(puts.strip())
# It is also used for the repetaion and concenation like making a \
# dynamic webpage header which lets user enter their and then changes teh websites name customized
name = "Umar"
print("Hello " + name)
print("-" * 20)

# String Formation :
#  It is also used for string formation 
# What: Inserting values into strings.
# How: f-strings, .format().
# Why: For clean, readable output.
# When: Displaying messages, reports.

user = "Umar"
score = 95
print(f"{user} scored {score} marks.")
# Real world use case: Generating the invoices of customers with customized names or collecting information 
customer = input("Enter your name: ")
amount = input("Enter the amount: ")
print(f"Invoice for {customer}: Total Rs.{amount}")


# Immutability
# What: Strings can’t be changed directly.
# How: You create a new string instead.
# Why: Safety — prevents accidental changes.
# When: Important in multi-threading and security
s = "Python"
# s[0] = "J" ❌ Not allowed
s = "J" + s[1:]  # ✅



print("📝 Practice Problems – Strings in Real Life")
# Problem no.01
# Username Greeting
# Ask the user for their name and print:
# Hello Umar, welcome to Python!

username = input("enter your name: ")
print(f"Hello! {username} Welcome to this organization")

# Problem no.02
# Ask the user for a word and a position (index), then print the character at that position.
word=input("Enter a word here: ")
number=int(input("Enter a number where you want to place the "))
print(word[number])

# word = input("Enter a word here: ")
# number = int(input("Enter a number (index) to get the letter: "))

# if 0 <= number < len(word):
#     print(f"The letter at index {number} is '{word[number]}'")
# else:
#     print(f"Invalid index! Please enter a number between 0 and {len(word)-1}")

# Problem no.03
#  Length of a Password
password= input("Enter the passowrd :")
print(len(password))

# Level 2 – Slicing & Indexing
# Extract Email Domain
# Input: "umar@gmail.com"
# Output: "gmail.com"
mail = input("Enter the gmail: ")
print(mail[4:])

# Hide Sensitive Data
sens_data = input("Enter : ")
print(sens_data.replace(sens_data ,"*" * len(sens_data)))

# Clean User Input
user_data = input('enter :')
print(user_data.lower())

# Check for Keyword
# Ask for a sentence and check if it contains the word "Python" (case-insensitive)
