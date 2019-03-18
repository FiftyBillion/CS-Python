def jogger(day):
    i = 0
    total = float(0)
    while i!= day:
        miles = float(input("Miles? "))
        total = total+miles
        i = i+1
    return total

days1 = int(input("Jogger 1: How many days? "))
total1 = jogger(days1)
print("Jogger 1's total miles =",format(total1,".1f"), "(",format(total1/days1,".1f"),"/ day)")

day2 = int(input("Jogger 2: How many day? "))
total2 = jogger(day2)
print("Jogger 2's total miles =",format(total2,".1f"), "(",format(total2/day2,".1f"),"/ day)")
print("Total points for both =", format(total1+total2,".1f"))

def inches2cm(inches):
    cm = inches*2.54
    return cm
for i in range(0,10):
    cm = inches2cm(i+1)
    print(i+1,"inches =",cm)

input("Press enter to exit")
