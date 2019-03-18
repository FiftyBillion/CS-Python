#Po-I Wu, Cheng Yi Tsai
#fortunes cookies
#this program tells your fortune

import random

print("Here is your special fortune cookie, it will tells your future.")
print("\nThe tag inside the cookie is:")

fortune = random.randint(1,10)

if fortune == 1:
    #good luck
    print("You will get marry really soon, and you will have two adorable childern.")

elif fortune == 2:
    #bad luck
    print("After you leave the restaurant, you gonna get robbed and your car had been stolen.")

elif fortune == 3:
    #money
    print("You will find 500$ this week.")

elif fortune == 4:
    #dog
    print("Your dog will eat your final project, so you will fail the class. HAHAHA!!!")

elif fortune == 5:
    #girl
    print("You will meet your Mr/Ms. Right next month. If you are single.")
elif fortune == 6:
    #direwolf
    print('You will become a die hard Game of Throne fan. And people around you will start shouting "THE KING OF THE NORTH"')
elif fortune == 7:
    #zombies
    print("Believe it or not, there will be a zombie disease break out two month later. Be prepared.")
elif fortune == 8:
    #iphone12ss
    print("You will be one of the Apple testing member and get to try out the latest Apple produt, Iphone12 doulbe S.")
elif fortune == 9:
    #dragon
    print("As you walk out of the restaurant, one of Daenerys' dragon will swallow you up.")
elif fortune == 10:
    #2016 election
    print("Donald Trump is going to win 2016 US president election, and become the last president of United States.")

input("\n\nPress the enter key to exit")
