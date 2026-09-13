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

def folderScan(userEnterFolderPath):
    new_hashes = {}
    contentsOfFolder = Path(userEnterFolderPath)
    for item in contentsOfFolder.iterdir():
        if item.is_file():
            with open(item, "rb") as file:
                digest = hashlib.file_digest(file, "sha256")
                finalHashResult = digest.hexdigest()
                new_hashes[item.name] = finalHashResult
    return new_hashes

def comparison(old_hashes, new_hashes): #requires parameters because the func doesn't know what we are iterating over
    for key in new_hashes:
        if key in old_hashes:
            if new_hashes[key] != old_hashes[key]:
                print(f"'{key}' was modified")
                global countModifiedFiles #to modify the variable inside the function, python will not think it as a new variable
                countModifiedFiles+=1
            else:
                print("File unchanged")
                global countUnchangedFiles
                countUnchangedFiles+=1
        if key not in old_hashes:
            print(f"New file detected: '{key}'")
            global countNewFilesDetected
            countNewFilesDetected+=1
                
    #Checking if the file is not in the new scanned result, if not then printing it's name
    for key in old_hashes:
        if key not in new_hashes:
            missingFile = key
            print(f"File deleted: {missingFile}")
            global countDeletedFiles
            countDeletedFiles+=1

try:
    if os.path.exists(filePath):
        old_hashes = load_json() 
        new_hashes = folderScan(userEnterFolderPath)
        comparison(old_hashes, new_hashes)
        printSummary()
    else:
        new_hashes = folderScan(userEnterFolderPath)
        with open(filePath, "w") as file:
            json.dump(new_hashes, file)
        print("File has been created\nPlease run the program again")

    update_json()

except FileNotFoundError:   
    print("Folder not found")

except json.JSONDecodeError:
    print("Json file is empty")

except NotADirectoryError:
    print("Not a folder")

#Note: This program doesn't read the sub-folders inside a directory, it'll be a feature for the upcoming commits.