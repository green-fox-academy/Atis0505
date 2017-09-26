class Tree(object):
    def __init__(self, color = "green", amount = 50):
        self.color = color
        self.amount = amount

    def watering(self):
        self.amount += 10
    
    def info(self):
        if self.amount > 85:
            print("The {} color tree doesn't need water.".format(self.color))
        else:
            print("The {} color tree needs water.".format(self.color))