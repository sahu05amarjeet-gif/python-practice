import json
file_path = "/home/amar/Documents/myself.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["work"])

except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You don't have the permission to read that file")

