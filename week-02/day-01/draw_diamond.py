# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was
lines = int(input("Number of lines: "))
stars = ""
spaces = ""
j = 1
for i in range(0, lines):
    for k in range(0, j):
        stars += "*"    
    for k in range(0, lines - i):
        spaces += " "
    print (spaces + stars + "\n")
    stars = ""
    spaces = ""
    j += 2

j = 2 * lines - 3
spaces = ""
stars = ""

for i in range(0, lines):
    for k in range(0, j):
        stars += "*"    
    for k in range(0, i+2):
        spaces += " "
    print (spaces + stars + "\n")
    stars = ""
    spaces = ""
    j -= 2