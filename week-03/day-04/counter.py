# Write a recursive function that takes one parameter: n and counts down from n.

def counter(number):
    if number <= 1:
        print(number)
        return 1
    else:
        print(number)
        return counter(number-1)

counter(10)