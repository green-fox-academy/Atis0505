import random
# Find out the number
#---------------------
# Create function for read the parameter
# Create function for randomed numbers
# Check the numbers
print("You have 5 lifes!")

def read_user_parameters(): 
    user_number = int(input("Your number(1-100): "))
    return user_number

def create_random_numbers():
    random_number = 0
    random_number = random.randint(1,100)
    return random_number


def check_numbers(read_user_parameters, create_random_numbers):
    if read_user_parameters == create_random_numbers:
        return 0
    elif read_user_parameters > create_random_numbers:
        return 1
    else:
        return -1


def user_message(check_numbers):
    random_numb = create_random_numbers
    life_number = 5
    for i in range(4):
        if life_number != 0:
            if check_numbers(read_user_parameters(), random_numb) == 1:
                print("My number is lower!")
            elif check_numbers(read_user_parameters(), random_numb) == 0:
                print("Congratulation!You found the number!")
                break
            else:
                print("My number is bigger!)
        else:
            print("GAME OVER DUDE!")

            
user_message(check_numbers(read_user_parameters(), create_random_numbers()))