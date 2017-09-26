class Aircraft(object):
    ammo = 0
    def __init__(self, aircraft_type):
        self.aircraft_type = aircraft_type
        if aircraft_type == "F16":
            self.maxammo = 8
            self.basedamage = 30
        elif aircraft_type == "F35":
            self.maxammo = 12
            self.basedamage = 50
    

    def fight(self):
        max_damage = self.ammo * self.basedamage
        self.ammo = 0
        return max_damage

    
    def refill(self, number):
        if self.aircraft_type == "F16":
            if self.maxammo > self.ammo:
                number -= (self.maxammo-self.ammo)
                return number
            else:
                return number
        elif self.aircraft_type == "F35":
            if self.maxammo > self.ammo:
                number -= (self.maxammo-self.ammo)
                return number
            else:
                return number


    def getType(self):
        print(self.aircraft_type)

    
    def getStatus(self):
        print("Type {}, Ammo: {}, Base Damage: {}, All Damage: {}".format(self.aircraft_type, self.ammo, self.basedamage, (self.maxammo*self.basedamage)))
    