import hashlib
from pathlib import Path

userEnterFolderPath = input("Enter the folder path: ")
hashes = {}
try:
    contentsOfFolder = Path(userEnterFolderPath)
    for item in contentsOfFolder.iterdir():
        if item.is_file():
            with open(item, "rb") as file:
                digest = hashlib.file_digest(file, "sha256")
                finalHashResult = digest.hexdigest()
                hashes[item.name] = finalHashResult
            # print(f"{item.name}: {finalHashResult}")
    print(hashes)
except FileNotFoundError:
    print("Folder not found")
except NotADirectoryError:
    print("Not a folder")

