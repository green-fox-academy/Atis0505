dogs_list = [
    {"name": "Lolka", "age":12},
    {"name": "Bodri", "age":7},
    {"name": "Dolly", "age":3},
    {"name": "Killer", "age":1}
]

def printer(dogs):
    for dog in dogs:
        print(dog["name"] + ", " + str(dog["age"]))
    print("")


def is_in_order(this, that):
    return this["age"] < that["age"]


def swapper(this, that):
    first = dogs_list.index(this)
    second = dogs_list.index(that)
    dogs_list[first], dogs_list[second] = dogs_list[second], dogs_list[first]


def bubble_sort(dogs):
    for i in range(len(dogs)):
        for j in range(len(dogs)-1-i):
            if not is_in_order(dogs[j], dogs[j+1]):
                swapper(dogs[j], dogs[j+1])

def ins_sort(dogs):
    for i in range(1,len(dogs)):
        j = i  
        while j > 0 and is_in_order(dogs[j], dogs[j-1]):
            swapper(dogs[j], dogs[j-1])
            j -= 1

ins_sort(dogs_list)
printer(dogs_list)