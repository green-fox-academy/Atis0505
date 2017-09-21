# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def numberadder(number):
    sum = number
    if number <= 1:
        return sum
    else:
        return sum + numberadder(number-1)


print(numberadder(5))