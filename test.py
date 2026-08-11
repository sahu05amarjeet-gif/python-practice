import os 
import json
import hashlib
password = []
salt = os.urandom(16)
salt_hex = salt.hex()
st_hash = hashlib.sha256(b"3214" + salt).hexdigest()
data = {
    "salt": salt_hex,
    "stored_hash": st_hash,
    "accounts": []
}
password.append(data)
file_path = "Practice/test.json"
with open(file_path, "w") as file:
    json.dump(password, file)
with open(file_path, "r") as file:
    pass_ = json.load(file)
    loaded_salt_hex = pass_[0]["salt"]
    converting = bytes.fromhex(loaded_salt_hex)
    loaded_hash = pass_[0]["stored_hash"]

user_input = input("Enter password: ").encode() 
hash_user = hashlib.sha256(user_input + converting).hexdigest()
if hash_user == loaded_hash:
    print("True")
