#Po-I Wu, Cheng Yi Tsai
#11/8/2016
#Homework 4-3
#This program read employees' hours and tell the total


#Employee 1
days = int(input("Employee 1: How many days? "))
total = 0 #so the hours can be added together, cumulatively

for day in range (0, days):
    hrs = float(input ("Hours? "))
    if hrs > 8:
        hrs = 8
    total = total + hrs
    per_day = total / days
print("Employee 1's total hours = ",int(total), \
      " (", format(per_day, '.2f')," hrs / day)", sep='')

#Employee 2
days = int(input("\nEmployee 2: How many days? "))
total_2 = 0

for day in range (0, days):
    hrs = float(input ("Hours? "))
    if hrs > 8:
        hrs = 8
    total_2 = total_2 + hrs
    per_day = total_2 / days
print("Employee 2's total hours = ",int(total_2), \
      " (", format(per_day, '.2f')," hrs / day)", sep='')

total_both = total + total_2

print("\nTotal hours for both =", int(total_both))

input("\nPress enter to continue.")
