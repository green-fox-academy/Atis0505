import random
# Find out the number
#---------------------
# Create function for read the parameter
# Create function for randomed numbers
# Check the numbers

def read_user_parameters():
    user_number = int(input("Your number(0-10): "))
    return user_number

def create_random_numbers():
    random_number = 0
    random_number = random.randint(0,10)
    return random_number

def check_numbers(read_user_parameters, create_random_numbers):
    if read_user_parameters == create_random_numbers:
        return True
    else:
        return False


def user_message(check_numbers):
    if check_numbers == False:
        print("This is not the number!!")
        print("Number was "+ str(create_random_numbers()))
    else:
        print("Congratulation! This is the number!!")

user_message(check_numbers(read_user_parameters(), create_random_numbers()))