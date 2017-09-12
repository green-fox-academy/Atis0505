# - Create a function called `factorio`
#   that returns it's input's factorial

n = int(input("Number: "))

def factorio(num):
    m = 1
    for i in range(1,(num+1)):
        m = m * i
    print("Factorio: ",m)    

factorio(n)