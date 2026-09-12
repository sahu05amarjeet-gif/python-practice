import hashlib
from pathlib import Path
import json
import os

countModifiedFiles = 0
countUnchangedFiles = 0
countNewFilesDetected = 0
countDeletedFiles = 0

filePath = "Practice/monitor.json"
def load_json(): #load the existing dictionaries from the monitor json file
    with open(filePath, "r") as file:
        loadedJson = json.load(file)
        return loadedJson
#saves the returned dictionary value into new_hashes

def update_json(): #dump the value into the monitor.json file
    with open(filePath, "w") as file:
        json.dump(new_hashes, file)

def printSummary():
    print("======================")
    print(f"Modified files: {countModifiedFiles}")
    print(f"Unchanged files: {countUnchangedFiles}")
    print(f"New files: {countNewFilesDetected}")
    print(f"Deleted files: {countDeletedFiles}")
    print("======================")

userEnterFolderPath = input("Enter the folder path: ")
new_hashes = {}
try:
    if os.path.exists(filePath):
        old_hashes = load_json() 
        contentsOfFolder = Path(userEnterFolderPath)
        for item in contentsOfFolder.iterdir():
            if item.is_file():
                with open(item, "rb") as file:
                    digest = hashlib.file_digest(file, "sha256")
                    finalHashResult = digest.hexdigest()
                    new_hashes[item.name] = finalHashResult

                #Check if the file exists in the old_hashes json file and then compare it.
                if item.name in old_hashes: 
                    if (new_hashes[item.name] != old_hashes[item.name]):
                        print(f"'{item.name}' was modified")
                        countModifiedFiles+=1
                    else:
                        print("File unchanged")
                        countUnchanedFiles+=1
                if item.name not in old_hashes:
                    print(f"New file detected: '{item.name}'")
                    countNewFilesDetected+=1

        #Checking if the file is not in the new scanned result, if not then printing it's name
        for key in old_hashes:
            if key not in new_hashes:
                missingFile = key
                print(f"File deleted: {missingFile}")
                countDeletedFiles+=1
    else:
        new_hashes = {}
        scanTheFolder = Path(userEnterFolderPath)
        for folder in scanTheFolder.iterdir():
            if folder.is_file:
                with open(folder, "rb") as file:
                    hashDigest = hashlib.file_digest("sha256")
                    finalHash = hashDigest.hexdigest()
                    new_hashes[folder.name] = finalHash

    printSummary()
    update_json()

except FileNotFoundError:   
    print("Folder not found")
except NotADirectoryError:
    print("Not a folder")



