#Po-I Wu
#11/25/2016
#Homework 6
#Counting program
#This program will count the numbers for the user

start = int(input('Enter a starting number: '))
end = int(input('Enter an ending number: '))
count_by = int(input('Enter the amount by which to count: '))
remainder = (end-start)%count_by
quotient = (end-start)//count_by

for i in range(start, end-remainder, count_by):
    print(i, end = ', ')
print(start+(quotient*count_by))

input('\nPress enter key to exit')
