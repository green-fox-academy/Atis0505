class Sharpie(object):
    def __init__(self, color, width):
        self.color = color
        self.width = float(width)
        self.ink_amount = 100

    def use(self):
        self.ink_amount -= 1

firstSharpie = Sharpie("black", 1.7)
secondSarphie = Sharpie("yellow", 2.1)

print(firstSharpie.color)
print(secondSarphie.ink_amount)
secondSarphie.use()
print(secondSarphie.ink_amount)