with open("notes.txt", 'w') as file:
    file.write("hello dear this is my first file handling line \n")
    file.write("Thsi is second line of my file handling learningn")

with open("notes.txt", 'r') as file:
    content = file.read()
    print(content)

with open('notes.txt' , 'a') as file:
    file.write("This line is appended int he fiel handling practice")


# Write Numbers from 1-10 :
with open("number.txt", 'w') as file:
    for i in range (1,11):
        file.write(str(i)+'\n')

with open("number.txt" , 'r') as file:
    print(file.read())



note = input("Enter a note for today: ")
date = input("Enter todays date: ")
with open("notebook.txt" , 'a') as file:
    file.write(f"Date is: {date} and the journal is: \n {note}")

with open("notebook.txt", 'r') as file:
    print(file.read())