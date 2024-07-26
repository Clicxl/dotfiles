from random import randint

randInt = randint(1,50)

userGuess = int(input("Guess A Number between 1 and 50: "))

if userGuess != randint:
  if userGuess > randInt:
    print("Guess a lesser number")
  else:
    print("Guess a higher number")
