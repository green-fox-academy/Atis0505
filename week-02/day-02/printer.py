# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)
n = int(input("Parameter: "))
m = input("Multiple?: ")

def printer(param, multi):
    
    if multi == 'y':
        print("The multiple number: "+str(param*2))
    else:
        print("The paramter: ",param)

printer(n,m)