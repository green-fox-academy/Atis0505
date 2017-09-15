import random


print("You have 5 lifes!")

def read_user_parameters(): 
    user_number = None
    while not type(user_number) == type(0):
        try:
            user_number = int(input("Your number(1-100): "))
            return user_number  
        except:
            print("This is not number!")


def create_random_numbers():
    random_number = 0
    random_number = random.randint(1,100)
    return random_number


def check_numbers(read_user_parameters, random_numbers):
    if read_user_parameters < random_numbers:
        value = -1
    elif read_user_parameters > random_numbers:
        value = 1
    else:
        value = 0
    return value


def user_message():
    random_numb = create_random_numbers()
    life_number = 4
    for i in range(5):
        user_number = read_user_parameters()
        if life_number != 0:
            if check_numbers(user_number, random_numb) == 1:
                print("My number is lower!")
                life_number -= 1
            elif check_numbers(user_number, random_numb) == -1:
                print("My number is bigger!")
                life_number -= 1
            else:
                
                print("Congratulation!You found the number!")
                break
        else:
            print("GAME OVER DUDE!")


user_message()
