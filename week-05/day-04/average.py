# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases


def odd_average(list_of_number):
    if len(list_of_number) == 0:
        return 0
    else:
        sum = 0
        for item in list_of_number:
            sum+= item
        average = sum/len(list_of_number)
        return average