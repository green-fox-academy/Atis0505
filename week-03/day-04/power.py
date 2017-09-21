# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def powerN(number, power):
    if power <= 0:
        return 1
    else:
        return number * powerN(number, power-1)

print(powerN(3,0))