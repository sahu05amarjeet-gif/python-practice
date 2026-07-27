import os 

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists")   #Relative
    if os.path.isfile(file_path):
        print("That is a file")

    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print("The file doesn't exists")

path = "/home/amar/Downloads"
if os.path.exists(path):
    print(f"The file '{path}' exists")   #Absolute

    if os.path.isfile(path):
        print("That is a file")

    elif os.path.isdir(path):
        print("That is a directory")

else:
    print("The path is wrong")
