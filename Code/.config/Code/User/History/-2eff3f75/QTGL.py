def display():
    count =0
    file = open("text.txt")
    for line in file:
        words = line.split()
        for W in words:
	        if W =="India":
	            count = count +1
                print(count)
    file.close()

display()
