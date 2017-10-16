# Create a function called `min_max_diff` that takes a list of numbers as parameter
# and returns the difference between maximum and minimum values in the list
# Create basic unit tests for it with at least 3 different test cases

def min_max_diff(number_list):
    if len(number_list) == 1:
        return number_list[0]
    elif type(number_list) == None:
        return False
    elif len(number_list) >= 2:
        max_number = max(number_list)
        min_number = min(number_list)
        diff_min_max = max_number - min_number
        return diff_min_max