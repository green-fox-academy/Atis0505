class Flower(object):
    def __init__(self, color = "green", amount = 50):
        self.color = color
        self.amount = amount

    def watering(self, amount = 0):
        self.amount += amount
    
    def info(self):
        if self.amount > 65:
            print("The {} color flower doesn't need water.".format(self.color))
        else:
            print("The {} color flower needs water.".format(self.color))