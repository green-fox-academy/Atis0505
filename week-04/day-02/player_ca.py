class Entity:
    def __init__(self):
        self.x = 22
        self.y = 33

    def talk(self):
        return 'I\'m at {}, {} location.'.format(self.x, self.y)


class Item:
    def __init__(self):
        self.inventory = [0,1,2]

    def add_item(self, item):
        self.inventory.append(item)

    def __str__(self):
        return str(self.inventory)

class Player(Entity, Item):
    def __init__(self):
        super().__init__()
        self.inventory = Item()
        self.inventory.add_item(12344)
        print(self.inventory.inventory)

    def talk(self, what):
        return 'I\'m at {}, {} location and saying {}.'.format(self.x, self.y, what)




ent = Entity()
print(ent.talk())
hero = Player()
print(hero.talk("'on the road again!'"))
print(hero.inventory)