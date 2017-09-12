# - Create a variable named `aj`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements in `aj`
# - Print the elements of the reversed `aj`
aj = [3, 4, 5, 6, 7]
for i in range(0,int((len(aj)/2))):
    aj[0+i],aj[-1-i] = aj[-1-i],aj[0+i]
print(aj)

# aj = list(reversed(aj))