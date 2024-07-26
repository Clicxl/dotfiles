import os

PATH = "/home/hrishikesh/Documents/Coding/javaScript/30Days/JavaScript30"

ignoreFiles = ['.gitignore','.md']
ignoreFolder = ['.git']

def removeIgnored(file):
    for ignore in ignoreFiles:
        if file == f"{PATH}/{ignore}":
            file.remove(ignore)

    for ignore in ignoreFolder:
        print("{file}:{f"{PATH}/{ignore}")
        if file == f"{PATH}/{ignore}":
            file.remove(ignore)


folder = []

for file in os.listdir(PATH):
        folder.append(f"{PATH}/{file}")

removeIgnored(folder)


# for each in folder:
#     print(os.listdir(each))

