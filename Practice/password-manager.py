import json
import string
import random
import hashlib
import os
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
        print("========== SAVED ACCOUNTS ==========")
        for index, password in enumerate(passwords, start=1):
            print(f"{index}.{password['website']}")

        print("=============================")
        choice = int(input("Enter account number: "))
        index = choice - 1
        result = passwords[index]['website']
        result2 = passwords[index]['username']
        result3 = passwords[index]['password']
        print("========== ACCOUNT DETAILS ==========")
        print(f"Website: '{result}'")
        print(f"Username: '{result2}'")
        print(f"Password: '{result3}'")
        print("=====================================")


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

max_attempts = 3
attempts = 0
program_running = True

file_path2 = "Practice/master-data.json"
if os.path.exists(file_path2):
    with open(file_path2, "r") as file:
        data = json.load(file)
        salt_from_data = data["salt"]
        converted_salt = bytes.fromhex(salt_from_data)
        loaded_hash = data["stored_hash"]
else:
    salt_master_data = os.urandom(16)
    salt_master_data_hex = salt_master_data.hex()
    master_pass = input("Don't have the master password? Create it: ").encode()
    salt_master_data_stored_hash = hashlib.sha256(master_pass + salt_master_data).hexdigest()
    data = {
        "salt": salt_master_data_hex,
        "stored_hash": salt_master_data_stored_hash
    }
    with open(file_path2, "w") as file:
        json.dump(data, file)
    converted_salt = salt_master_data
    loaded_hash = salt_master_data_stored_hash

while attempts < max_attempts and program_running:
            enter_master_pass = input("Enter the master password: ").encode()
            entered_hash = hashlib.sha256(enter_master_pass + converted_salt).hexdigest()
            if entered_hash == loaded_hash:
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
                        program_running = False
                    else:
                        print("Not a valid choice")
            else:
                attempts += 1
                remaining = max_attempts - attempts
                print(f"{remaining} attempt(s) left")

            if attempts == max_attempts:
                print("Access denied!")
                program_running = False

