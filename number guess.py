#Po-I Wu, cheng Yi Tsai
#Homework 5-2
#progarm guessing game
#11/10/2016
#this program is a game for user try to guess a number 1 to 100
#And it will tell you how many times have you tried
#Try to beat your records!!!
print("Welcome to the number guessing game.")
print("The object is to guess the unmber 1 to 100.")

import random
number = random.randint(1,50)

guess = int(input("What is your first guess?"))

guesses = 1

while guess != number:
    if guess > number:
        print("lower!")
    else:
        print("higher!")

    guess =int(input("What is your next guess??"))
    guesses += 1

print("Good job!!! You got the number right!!! You gave", guesses,"tries.")
input("\nPress enter key to exit.")
