import random as ra
import string as st

chars = " " + st.ascii_letters + st.punctuation + st.digits + st.hexdigits
chars = list(chars)

key = chars.copy()

ra.shuffle(key)
# print(f"chars: ", chars)
# print(f"keys: ", key)

#ENCRYPT 
letters = input("Enter the message to encrypt: ")
cipher_text = ""

for letter in letters:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original Message: {letters}")
print(f"Encrypted Message: {cipher_text}")


#DECRYPT
cipher_text = input("Enter the message to decrypt: ")
letters = ""

for letter in cipher_text:
    index = key.index(letter)
    letters += chars[index]

print(f"Original Message: {cipher_text}")
print(f"Decrypted message: {letters}")
