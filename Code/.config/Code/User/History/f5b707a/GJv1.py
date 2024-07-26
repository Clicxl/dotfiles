import os

PATH = "/home/hrishikesh/Documents/Coding/javaScript/30Days/JavaScript30"

ignoreFiles = ['.gitignore','.md']
ignoreFolder = ['.git']

folder = []

for file in os.listdir(PATH):
    
        folder.append(f"{PATH}/{file}")



def removeIgnored(file):
    for ignore in ignoreFiles:
        if file == f"{PATH}/{ignore}":
            file.remove(ignore)

    for ignore in ignoreFolder:
        if file == f"{PATH}/{ignore}":
            file.remove(ignore)

removeIgnored(folder)
print(folder)

