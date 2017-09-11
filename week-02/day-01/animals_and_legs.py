# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have
chickens = int(input("Chicken: "))
pigs = int(input("Pig: "))

print("Legs number: " + (str(2*chickens + 4*pigs)))