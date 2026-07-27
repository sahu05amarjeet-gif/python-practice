user = int(input("Enter the number: "))

file_path = "multiplication.txt"

with open(file_path, "w") as file:
    for x in range(1, 11):
        total = user * x
        line = f"{user} x {x} = {total}"
        file.write(str(line) + "\n")
        

    print("The file has been created")
        
