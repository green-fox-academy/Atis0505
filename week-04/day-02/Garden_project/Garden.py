from Flower import Flower
from Tree import Tree

class Garden:
    def __init__(self):
        self.list_of_flowers = []
        self.list_of_trees = []

    
    def add_flower(self, flower):
        self.list_of_flowers.append(flower)

    
    def add_tree(self, tree):
        self.list_of_trees.append(tree)

    
    def watering(self, amount=0):
        for i in range(len(self.list_of_flowers)):
            self.list_of_flowers[i].watering(amount)
            self.list_of_flowers[i].info()

        for j in range(len(self.list_of_trees)):
            self.list_of_trees[j].watering(amount)
            self.list_of_trees[j].info()
    
garden = Garden()

flower01 = Flower("blue", 25)
garden.add_flower(flower01)
flower02 = Flower("yellow", 34)
garden.add_flower(flower02)
flower03 = Flower("red", 45)
garden.add_flower(flower03)
tree01 = Tree("brown", 56)
garden.add_tree(tree01)
tree02 = Tree("dark brown", 67)
garden.add_tree(tree02)
tree03 = Tree("black", 78)
garden.add_tree(tree03)

garden.watering(10)
print()
garden.watering(20)
print()
garden.watering(25)


