#Po-I Wu
#11/25/2016
#Homework 6
#Guessing program
#This program will create a random number
#and the user can guess it

import random

def ask_number(question, low, high):
    """Ask for a number within a range."""
    number = random.randint(lower, higher)
    guesses = 1
    response = question
    while response != number:
        if response < number:
            print("too low")
        else:
            print("too high")
        response = int(input("Please guess again: "))
        guesses = guesses + 1
    if response==number:
        print("You are correct!")        
    return guesses

play = input("Do you want to play this game? Y/N:")
while play.lower() == "y":
    lower = int(input('From: '))
    higher = int(input('To: '))
    question1 = int(input('What is your first guess? '))
    ask_number(question1, lower, higher)
    play = input("Do you want to play this game? Y/N: ")

input("Bye bye. Press enter to exit...")
