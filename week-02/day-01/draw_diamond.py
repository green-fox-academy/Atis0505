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

for i in range(1, int(2*number1)):
    if number1 % 2 == 1 and number1 != 0 and i <= number1:
        for m in reversed(range(int(number1//2)-1)):
            print(space*m + star*i)
