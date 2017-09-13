# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
check_numbers = [4,8,12,16]

equal_num = 0
for n in list_of_numbers:
    for m in check_numbers:
        if equal_num < len(check_numbers):
            if n == m:
                equal_num+=1
if equal_num == len(check_numbers):
    print("True")
else:
    print("False")            