# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.
number = int(input("Number: "))
if number % 2 == 0 and number != 0:
    print("Even")
elif number % 2 == 1:
    print("Odd")
else:
    print("Zero")