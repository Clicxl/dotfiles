import os

PATH = "/home/hrishikesh/Documents/Coding/javaScript/30Days/JavaScript30"

ignoreFiles = ['.gitignore','.md']
ignoreFolder = ['.git']

paths = f"{PATH}/{os.listdir(PATH)}"


def removeIgnored(paths):
    for ignore in ignoreFiles:
        for file in paths:
            if file == f"{PATH}/{ignore}":
                paths.remove(ignore)

    for ignore in ignoreFolder:
        for file in paths:
            if file == "{PATH}/{ignore}":
                paths.remove(ignore)

removeIgnored(paths)
print

for folder in paths:
    print(folder)