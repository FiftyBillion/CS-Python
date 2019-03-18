#Po-I Wu
#11/27/2016
#Homework 6
#backwards program
#This program print the message backwards

message = input("Enter the messsage: ")
output = ''

for a in message:
    output = a + output
print(output)

input('\nPress enter to exit.')
