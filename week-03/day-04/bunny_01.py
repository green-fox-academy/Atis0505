# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def bunny_ear_counter(bunny_number):
    if bunny_number <= 1:
        return 2
    else:
        return 2 + bunny_ear_counter(bunny_number-1)

print(bunny_ear_counter(20))