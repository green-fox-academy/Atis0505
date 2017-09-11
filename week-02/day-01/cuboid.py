# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000
a = int(input("Kérem az a oldalt: \n"))

print("Surface area: " + str(a*6) + "\n")
print("Volume: " + str(a**3))