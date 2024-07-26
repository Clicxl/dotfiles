def display():
    count = 0
    file = open("text.txt")
    for line in file:
        words = line.split()
        print(words, end="")


display()
