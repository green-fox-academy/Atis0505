# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

def bunny_ear_counter(bunny_number):
    if bunny_number <= 1:
        return 2
    elif bunny_number%2 == 0:
        return 3 + bunny_ear_counter(bunny_number-1)
    else:
        return 2 + bunny_ear_counter(bunny_number-1)


print(bunny_ear_counter(5))        