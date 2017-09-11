# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was
number1 = int(input("Number: "))
space = " "
prezent = "%"
for i in range(1, number1):
    if i == 1:
        print(prezent*number1)
    elif i == (number1-1):
        print(prezent*number1)
    else:
        m = 0
        for n in range(2, int(number1-1)):
            print(prezent + space*m + prezent)
            m += 1
