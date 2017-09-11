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
number1 = int(input("Number: "))
star = "*"
space = " "
m = 0
for j in range(1, (2*number1+1)):
    if j % 2 == 1 and j != 0 and j <= number1:
        print(space*(number1//2-m) + star*(j))
        m += 1
    elif j % 2 == 1 and j > number1:
        n = number1
        for i in range(1, number1):
            m -= 2
            print(space*i + star*m)
            