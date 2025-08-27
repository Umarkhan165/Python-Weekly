# with open("notes.txt", 'w') as file:
#     file.write("hello dear this is my first file handling line \n")
#     file.write("Thsi is second line of my file handling learningn")

# with open("notes.txt", 'r') as file:
#     content = file.read()
#     print(content)

# with open('notes.txt' , 'a') as file:
#     file.write("This line is appended int he fiel handling practice")


# # Write Numbers from 1-10 :
# with open("number.txt", 'w') as file:
#     for i in range (1,11):
#         file.write(str(i)+'\n')

# with open("number.txt" , 'r') as file:
#     print(file.read())



# note = input("Enter a note for today: ")
# date = input("Enter todays date: ")
# with open("notebook.txt" , 'a') as file:
#     file.write(f"Date is: {date} and the journal is: \n {note}")

# with open("notebook.txt", 'r') as file:
#     print(file.read())

# with open("D:\Python Weekly\Week 04\demo.txt" , 'r') as f:
#     print(f.read())
#     f.close()

# # Return irst 5 charcters :
# with open("D:\Python Weekly\Week 04\demo.txt" , 'r') as f:
#     print(f.read(5))
#     f.close()

# # You can return one line by using the readline() method:
# with open("D:\Python Weekly\Week 04\demo.txt" , 'r') as f:
#     print(f.readline())
#     f.close()
# # same by using readline() two times we can read more lines:
# with open("D:\Python Weekly\Week 04\demo.txt" , 'r') as f:
#     print(f.readline())
#     print(f.readline())
#     f.close()

# By looping through the lines of the file, you can read the whole file, line by line
# with open("D:\Python Weekly\Week 04\demo.txt" , 'r') as f:
#     for x in f:
#         print(x)

# # Write to an Existing File

# # "a" - Append - will append to the end of the file

# # "w" - Write - will overwrite any existing content

# with open("D:\Python Weekly\Week 04\demo.txt" , 'a') as f:
#     f.write("This is teh next line i am adding suing append")
    
# with open("D:\Python Weekly\Week 04\demo.txt") as f:
#   print(f.read())

# # For Overwriting the file:
# with open("demofile.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")

# #open and read the file after the overwriting:
# with open("demofile.txt") as f:
#   print(f.read())


