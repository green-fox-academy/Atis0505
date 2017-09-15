# Armstrong number?

number_input = input("The number: ")


def main_function(int_input):
    sum_number = 0
    for i in range(len(int_input)):
        sum_number += int(int_input[i]) ** int(len(int_input))
    if sum_number == int(int_input):
        print("The number " + str(sum_number) + " is Armstrong number!")
    else:
        ("This is not Armstrong number!")


main_function(number_input)