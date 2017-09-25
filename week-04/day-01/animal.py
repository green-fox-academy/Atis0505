class Animal(object):
    def __init__(self):
        self.hunger = 50
        self.thirst = 50


    def eat(self):
        self.hunger += 1
        return print(self.hunger)


    def drink(self):
        self.thirst += 1
        return print(self.thirst)

    
    def play(self):
        self.hunger += 1
        self.thirst += 1
        return print("hungry: " + str(self.hunger)+", thirst: "+str(self.thirst))

    
kutya = Animal()
macska = Animal()

kutya.eat()
macska.drink()

kutya.play()

