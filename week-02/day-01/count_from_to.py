# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
if number1 < number2:
    for i in range(number1,number2):
        print(i)
else:
    print("The second number should be bigger")