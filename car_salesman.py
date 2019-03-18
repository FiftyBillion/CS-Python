#Po-I Wu
#10/16/2016
#Homework 2
#Enter the price of a car
#The program will calculate the total amount
#which included tax, license, dealer prep, and destination charge


price_of_car = float(input("Please enter the original price of a car: $"))

tax = price_of_car * 0.11
license_fee = price_of_car * 0.08
dealer_prep = 103
destination_charge = 209
                            
print("\nTax: $" + format(tax, '.2f'))
print("\nLicense: $" + format(license_fee, '.2f'))
print("\nDealer prep: $" + format(dealer_prep, '.2f'))
print("\nDestination charge: $" + format(destination_charge, '.2f'))

print("\nThe total amount is: $" + format(price_of_car + tax + license_fee + dealer_prep + destination_charge, '.2f'))

input("\n\nPress the enter key to exit")
