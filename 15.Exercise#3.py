# username validate programm


username = input("Enter your username: ")

if(len(username)>12):
    print("Your username should not contain more than 12 characters")
elif not (username.find(" ")==-1):
    print("Your username should not contain any spaces")
elif not (username.isalpha()):
    print("Your username should not contain any digits")
else:
    print(f"Welcome, {username}")
