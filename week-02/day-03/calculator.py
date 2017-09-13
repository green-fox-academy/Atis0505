# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit
op, n, m = input("Give me datas separatly with \"-\": ").split("-")

# num01 = int(input("First number: "))
# num02 = int(input("Second number: "))
# op = str(input("Operation: "))
num01 = int(n)
num02 = int(m)

def add():
    print(num01+num02)
def subs():
    print(num01-num02)
def div():
    print(num01/num02)
def multi():
    print(num01*num02)
def mod():
    print(num01%num02)

operation = {
    "+" : add,
    "-" : subs,
    "/" : div,
    "*" : multi,
    "%" : mod,
}

operation[str(op)]()