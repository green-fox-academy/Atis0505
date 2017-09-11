# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

number1 = int(input("First number: "))
star = "*"
for j in range(1, (number1+1)):
    print(star*(j))