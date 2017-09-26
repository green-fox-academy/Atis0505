class Tree(object):
    def __init__(self, color = "green", amount = 50):
        self.color = color
        self.amount = amount

    def watering(self, amount = 0):
        self.amount += amount
    
    def info(self):
        if self.amount > 85:
            print("The {} tree doesn't need water.".format(self.color))
        else:
            print("The {} tree needs water.".format(self.color))