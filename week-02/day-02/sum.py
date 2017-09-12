# - Write a function called `sum` that sum all the numbers
#   until the given parameter

n = int(input("Kérem a számot: "))

def sum(num):
    for i in range(1, num):
        print(i)
sum(n)