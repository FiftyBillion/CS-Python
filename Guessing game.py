#Po-I Wu
#program guessing game
#This program is a game where the user tries
#to guess a number between 1 and 100

print("Welcome to the number guessing game!!\n")
print("The object is to guess a number between 1 and 100")

import random
number = random.randint(1,100)

guess = int(input("What's your first guess?"))

guesses = 1

while guess != number:
    if guess > number:
        print("You need to guess lower than that!")
    else:
        print("You need to guess higher than that!")
        
    guess = int(input("What's your next guess?"))
    guesses += 1

print("\nCongratulations!! You got the number right!!\n\
It only took you", guesses,"tries!!")

input("\nPress enter to exit.")
