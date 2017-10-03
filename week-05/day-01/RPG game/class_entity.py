

class Entity(object):
    def __init__(self, cordX, cordY):
        self.X = cordX
        self.Y = cordY


class Hero(Entity):
    def __init__(self, X = 35, Y = 35 ):
        super().__init__( X, Y)
       

    
