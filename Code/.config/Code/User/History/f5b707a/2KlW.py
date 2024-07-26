import os

PATH = "/home/hrishikesh/Documents/Coding/javaScript/30Days/JavaScript30"

ignoreFiles = ['.gitignore','.md']
ignoreFolder = ['.git']

folder = []

for file in os.listdir(PATH):
        folder.append(f"{PATH}/{file}")



def removeIgnored(file):
    for ignoredfile,ignoredfolder in ignoreFiles,ignoreFolder:
        if file == f"{PATH}/{ignoredfile}":
            file.remove(ignoredfile)

# removeIgnored(folder)
print(folder)

