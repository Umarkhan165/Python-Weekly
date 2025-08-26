# f = open("notes.txt", 'r')
# data = f.read()
# print(data)
# print(type(data))
# f.close()


#  For reading first fuve words of teh file :
# f = open("notes.txt", 'r')
# data = f.read(5)
# print(data)
# print(type(data))
# f.close()

#  Reading Lines:
# f = open("notes.txt", 'r')
# line1 = f.readline()
# print(line1)

# line2 = f.readline
# print(line2)

# f = open("notes.txt", 'a')
# f.write("\nThis is what i have written using the append mode.")
# f.close()

# we can aslo use with method for this :

#  Module Creation:

# import os
# os.remove("sample.txt")

with open("Practice.txt", 'w') as file:
    data = file.write("This is data one , \n THis is line 2 \n This is line 3")
    datas = file.readlines()
    print(datas)


