# Create a function that takes a list of numbers as a parameter
# Returns a list of numbers where every number in the list occurs only once

# Example

# input: [1, 11, 34, 11, 52, 61, 1, 34]
# output: [1, 11, 34, 52, 61]

numbers = [1, 11, 34, 11, 52, 61, 1, 34]

def remove_duplicate(num_list):
    num_back_list = []
    for n in num_list:
        if not n in num_back_list:
            num_back_list.append(n)
    print(num_back_list)

remove_duplicate(numbers)