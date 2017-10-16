import sys

user_input = sys.argv

def check_user_inputs(user_input):
    if len(user_input) == 1:
        return print_user_optons()
    elif len(user_input) < 4:
        return print("Missing arguments!")
    elif len(user_input) > 4:
        return print("Too much inputs!")
    else:
        return check_arguments(user_input)


def check_arguments(user_arguments):
    operator_list = ["+", "-", "*", "/"]
    if user_arguments[1] not in operator_list:
        return print("This operator is not allowed!")
    else:
        return {
        "+": add,
        "-": subst,
        "*": multiple,
        "/": divi,
        }[user_arguments[1]](int(user_arguments[2]), int(user_arguments[3]))


def add(numA, numB):
    result = numA + numB
    print(result)
    return result


def subst(numA, numB):
    result = numA - numB
    print(result)
    return result


def multiple(numA, numB):
    result = numA * numB
    print(result)
    return result


def divide(numA, numB):
    result = numA / numB
    return result

def divi(numA, numB):
    try:
        result = numA / numB
        return result
    except ZeroDivisionError:
        print("Divide by 0 is not an interpreted operation")
        return 0

def print_user_optons():
    print("""
    Use first operator, and after write 2 numbers!
    """)


check_user_inputs(user_input)