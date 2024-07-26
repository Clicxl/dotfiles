import os

PATH = "/home/hrishikesh/Documents/Coding/javaScript/30Days/JavaScript30"

ignoreFiles = ['.gitignore','.md']
ignoreFolder = ['.git']

def removeIgnored(folder):
    for ignore in ignoreFiles:
        for file in folder:
            if file == f"{PATH}/{ignore}":
                print(f"{file} : {PATH}/{ignore}")
                folder.remove(ignore)

    for ignore in ignoreFolder:
        for file in folder:
            if file == f"{PATH}/{ignore}":
                print(f"{file} : {PATH}/{ignore}")
                folder.remove(ignore)


folder = []

for file in os.listdir(PATH):
        folder.append(f"{PATH}/{file}")

removeIgnored(folder)


# for each in folder:
#     print(os.listdir(each))

