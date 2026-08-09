
# import json
# employees = {
#      "name": "Amar",
#      "age": 20,
#      "work": "cybersec engineer"
# }

# file_path = "/home/amar/Documents/myself.json"
# try: 
#     with open(file_path, "w") as file:
#           json.dump(employees, file, indent=4)
#           print("The json file has been created")

# except FileExistsError:
#         print("The file already exists")

file_path = "/home/amar/Documents/test1.txt"

with open(file_path, "w") as file:
    file.write("Hello World")

with open(file_path) as file:
    print(file.read())

