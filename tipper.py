#Po-I Wu
#10/16/2016
#Homework 2
#After enter the bill total
#This will calculate a 15 percent tip and a 20 percent tip

print("Hi, I will calculate the tips for you")

total_bill = float(input("\nPlease enter your total bill amount: $"))

tip_1 = total_bill * 0.15
tip_2 = total_bill * 0.2
print("\n15 percent tip: $", format(tip_1, '.2f'), sep = "")
print("\n20 percent tip: $", format(tip_2, '.2f'), sep = "")

input("\n\nPress the enter key to exit")
