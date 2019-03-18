#Cheng Yi Tsai, Po-I Wu
#Homework 5-1 Coin flip
#11/14/2016
#This progarm flips the coin for you and tells you how many times you fliped heads and tails 

import random

total_heads = 0
total_tails = 0
tries = 0

print("Flip the corn 100 times:\n")

while tries < 100:
    coin = random.randint(1,2)

    if coin == 1: #heads as 1
        print("Heads!\n") 
        total_heads += 1
        tries += 1
    elif coin == 2: #tails as 2
        print("Tails!\n")
        total_tails += 1
        tries += 1

print("\nSO you have flipped heads", total_heads, "times.")
print("\nAnd you have flipped tails", total_tails, "times.")

input("Press enter to continue")
