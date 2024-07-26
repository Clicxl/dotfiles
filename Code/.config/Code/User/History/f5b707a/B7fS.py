import os

PATH = "/home/hrishikesh/Documents/Coding/javaScript/30Days/JavaScript30"

ignoreFiles = ['.gitignore','.md']
ignoreFolder = ['.git']

paths = os.listdir(PATH)


def removeIgnored(paths):
    for ignore in ignoreFiles:
        for file in paths:
            if file == ignore:
                paths.remove(ignore)

    for ignore in ignoreFolder:
        for file in paths:
            if file == ignore:
                paths.remove(ignore)

removeIgnored(paths)

for folder in paths:
    fullName = f"{PATH}/{folder}"
    print(os.path(fullName))