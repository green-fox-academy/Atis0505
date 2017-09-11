# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
number1 = int(input("Number: "))
star = "*"
space = " "
m = 0
for j in range(1, (number1+1)):
    if j % 2 == 1 and j != 0:
        print(space*(number1//2-m) + star*(j))
        m += 1