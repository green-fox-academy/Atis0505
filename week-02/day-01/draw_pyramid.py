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
c=5
k = "*"
j="h"
d=5//2

for i in range(0,d):
    t=c-(2*d)
    print(j*d+t*k+j*d)
    
    