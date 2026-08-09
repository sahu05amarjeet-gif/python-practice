import json
import string
import random
file_path = "/home/amar/Amarjeet/Backup 26th Feb/Python/Practice/passwords.json"
with open(file_path, "r") as file:
    passwords = json.load(file)
is_running = True


def update_json():
    with open(file_path, "w") as file:
        json.dump(passwords, file)

def add_password():
    print("------------------------")
    web_info = input("Website: ")
    username = input("Username: ")
    running = True
    while running:
            ask_user_for_pass = input("Generate Password automatically? (Y/N): ").upper()
            if ask_user_for_pass == "Y":
                pass_word = generate_password()
                print(f"'{pass_word}' The password has been generated automatically")
                print("--------------------------------------------------------------")
                running = False
            elif ask_user_for_pass == "N":
                pass_word = input("Password: ")
                running = False
            else:
                print(f"{ask_user_for_pass} is not a valid choice, Try again!")
                

    account = {
        "website": web_info,
        "username": username,
        "password": pass_word
    }

    passwords.append(account)
    update_json()
    print("Password saved!")
    print("------------------------")
    
def view_password():
    for password in passwords:
        print("--------------------------------")
        print(f"Website: {password['website']}")
        print(f"Username: {password['username']}")
        print(f"Password: {password['password']}")
        print("--------------------------------")

def search_password():
    print("---------------------------------------------------------------")
    found = False
    user_ask = input("Enter the name of website you're looking for: ")
    for pass_ in passwords:
        if user_ask in pass_["website"]:
            print(f"Fetched Password: {pass_['password']}")
            print(  "-------------------------------------------------------")
            found = True
    if not found:
        print(f"'{user_ask}' doesn't exists")
def delete_password():
    ask_remove = input("Enter the name of the website you want to delete: ")
    for remove_pass in passwords:
        if ask_remove in remove_pass['website']:
            passwords.remove(remove_pass)
            update_json()
            print("Password removed!")
        else:
            print(f"'{ask_remove}' doesn't exists")

def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    punctuations = string.punctuation

    letter = random.choice(letters)
    digit = random.choice(digits)
    punctuation = random.choice(punctuations)

    chars = letters + digits + punctuations

    data = letter + digit + punctuation
    data = list(data)
    for x in range(1, 10):
        data.append(random.choice(chars))
    random.shuffle(data)
    return "".join(data)

while is_running:
    print("1. Add Password")
    print("2. View Password")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")
    choose = int(input("Choose: "))
    if choose == 1:
        add_password()
    elif choose == 2:
        view_password()
    elif choose == 3:
        search_password()
    elif choose == 4:
        delete_password()
    elif choose == 5:
        is_running = False
    else:
        print("Not a valid choice")

