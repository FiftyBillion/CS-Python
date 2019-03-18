#Po-I Wu
#program cylinder
#this calculate the volume of a cylinder!

import math

def cyl_volume(radius,height):
    volume = (math.pi)*radius**height
    return volume

rad = float(input("What is the radius of the cylinder?\n"))
ht = float(input("What is the height of the cylinder?\n"))

vol = cyl_volume(rad,ht)

print("\nThe volume of your cylinder is", vol)
