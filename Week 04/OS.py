# Create a New File
f = open("file_using_x.txt", 'x')

# Delete a File

import os
os.remove("file_using_x.txt")

# Check if File exist:
f = open("file_using_x.txt", 'x')
import os 
if os.path.exists("file_using_x.txt"):
    os.remove("file_using_x.txt")
else:
    print("File does not exist")

# Delete Folder
import os 
os.rmdir("myfolder")