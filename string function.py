#Po-I Wu, Cheng Yi Tsai
#Homework 5-3
#11/9/2016
#This program demonstrate string function

sentence = "           haha! Welcome to this Bla Bla Bla program!!           "

print(sentence)

print("\nUsing 'upper()' will be like:\n"+sentence.upper())

print("\nUsing 'swapcase()' will be like:\n"+sentence.swapcase())

print("\nUsing 'title()' will be like:\n"+sentence.title())

print("\nUsing 'replace('l','r', 4)' will be like:\n"+sentence.replace('l','r',4))

print("\nUsing 'strip()' will be like:\n"+sentence.strip())

print("\nUsing 'capitalize()' will be like:\n"+sentence.capitalize())

print("\n---because we used space as first word, all change it to lowercase...\n\
   Let's try strip and capitalize togather!!")

print("\nUsing 'strip().capitalize()' will be like:\n"+sentence.strip().capitalize())

input("\nPress enter to exit.")
