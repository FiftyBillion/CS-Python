#Po-I Wu
#10/19/16
#Homework 3-2
#The dark room program(fix the code)
#Dicide a room which you want to get in
#Then you can see what happen

print("You enter a dark room with two doors.\nDo you go through door #1 or door #2?")

door = input()

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input()

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)
        print("Then, you saw a big door.")
        print("Press enter to get in...")

        big_door = input()

        if big_door == "":
            print("WOW!!! Now you see a gate to exit, but it requires a password.")
            print("There is a hint on the door.")
            print("\n\n1+1=")
            print("2+2=")
            print("3+3=")
            print("3*3=")

            password = input("\nPlease enter the password to exit:")

            if password == "2469":
                print("\nSuccess!!")
                print("The gate is opened, congratulation!")
            else:
                print("Wrong password.")
                print("And you died......")

elif door == "2":
    print("You stare into the endless abyss at Cthlhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input()

    if insanity == "1" or insanity == "2":
        print("Your body survive powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")


else:
    print("You stumble around and fall on a knife and die. Good job!")

input("Press enter to continue")
