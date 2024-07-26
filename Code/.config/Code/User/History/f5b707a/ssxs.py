import os

PATH = "/home/hrishikesh/Documents/Coding/javaScript/30Days/JavaScript30"

ignoreFiles = ['.gitignore','.md']
ignoreFolder = ['.git']
ignoreTags = ['.html',".css",".js"]

def removeIgnored(folder):
    for ignore in ignoreFiles:
        for file in folder:
            if file[-3:len(file)] == f"{PATH}/{ignore}"[-3:len(file)]:
                folder.remove(file)
                # print(f"{file} Removed")

    for ignore in ignoreFolder:
        for file in folder:
            if file == f"{PATH}/{ignore}":
                folder.remove(file)
                # print(f"{file} Removed")


folder = []

for file in os.listdir(PATH):
        folder.append(f"{PATH}/{file}")

removeIgnored(folder)


for each in folder:
    print(os.listdir(each))

