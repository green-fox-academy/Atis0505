import random

class Sharpie(object):
    def __init__(self, color, width, ink_amount = 10):
        self.color = color
        self.width = float(width)
        self.ink_amount = ink_amount

    def use(self):
        self.ink_amount -= 1
        return self.ink_amount

class SharpieSet(object):
    def __init__(self, list_of_sharpie):
        self.list_of_sharpie = list_of_sharpie


    def count_usable(self):
        usable_sharpie = 0
        for i in range(len(self.list_of_sharpie)):
            if self.list_of_sharpie[i].ink_amount > 90:
                usable_sharpie += 1
        return usable_sharpie


    def remove_trash(self):
        remove_list = []
        removed_sharpie = 0
        for i in range(len(self.list_of_sharpie)):
            if self.list_of_sharpie[i].ink_amount <= 90:
                remove_list.append(self.list_of_sharpie[i])
                removed_sharpie +=1
                print(remove_list)
        
        return removed_sharpie

    def printer(self):
        for i in range(len(self.list_of_sharpie)):
            print(str(self.list_of_sharpie[i].ink_amount))

def create_sharpie_list():
    sharpie_list = []
    for i in range(6):
        sarphie = Sharpie("yellow", i*i, 100-(i*i))
        sharpie_list.append(sarphie)
    return sharpie_list

sarphies_obj = SharpieSet(create_sharpie_list())
sarphies_obj.printer()
print(sarphies_obj.count_usable())
print(sarphies_obj.remove_trash())
