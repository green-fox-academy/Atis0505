# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was
number1 = int(input("Number: "))

for i in range(1,number1):
    for j in range(1,number1):
        if (i == 1 or i == number1) and (j == 1 or j == number1):
            print("%")
        
        