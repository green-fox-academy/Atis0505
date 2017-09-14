# Find the part of int

# Create a function that takes a number and a list of numbers as a parameter
# Returns the indeces of the numbers in the list where the first number is part of
# Returns an empty list if the number is not part any of the numbers in the list
# Example

# input: [1, 11, 34, 52, 61], 1
# output: [0, 1, 4]

numbers = [1, 11, 34, 52, 61]
numb = 1

def number_finder(a, numb_list):
    string_list=[]
    index_list = []
    for n in range(len(numb_list)):
        string_list.append(str(numb_list[n]))
    for i in range(len(numb_list)):
        flag = True
        for j in range(len(string_list[i])):
            if string_list[i][j] == str(a) and flag:
                index_list.append(i)
                flag = False

    print(string_list)
    print(index_list)

number_finder(numb, numbers)