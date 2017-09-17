# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0
def read_user_parameter():
    try:
        user_number = int(input("The number: "))
        print(10/user_number)
        
    except ZeroDivisionError:
        print("Fail")

read_user_parameter()