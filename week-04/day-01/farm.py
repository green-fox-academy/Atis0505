from animal import Animal

class Farm(object):
    def __init__(self, list_of_animal, place_number):
        self.list_of_animal = list_of_animal
        self.place_number = place_number
    
    def breed(self):
        if len(self.list_of_animal) == self.place_number:
            print("You have enough animal.")
        elif len(self.list_of_animal) >= self.place_number:
            print("You have too much animals!")
        else:
            for i in range((self.place_number-len(self.list_of_animal))):
                self.list_of_animal.append(Animal(i*5,i*10))
        print(len(self.list_of_animal))
            

    def slaughter(self):
        max = 0
        for i in range(len(self.list_of_animal)):
            if self.list_of_animal[i].hunger > max:
                max = self.list_of_animal[i].hunger
            print(str(self.list_of_animal[i].hunger))
        


def create_animal():
    animal_list = []
    for i in range(6):
        animal_list.append(Animal(i*10,i*15))
    return animal_list


farm_01 = Farm(create_animal(), 10)
print(str(len(create_animal())))
print(str(len(farm_01.list_of_animal)))
farm_01.breed()
print(str(len(farm_01.list_of_animal)))
farm_01.slaughter()
