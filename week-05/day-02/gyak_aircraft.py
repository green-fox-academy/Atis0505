class Aircraft(object):
    def __init__(self, aircraft_type):
        self.aircraft_type = aircraft_type
        self.ammo = 0
        if aircraft_type == "f16":
            self.max_ammo = 8
            self.base_damage = 30
        elif aircraft_type == "f35":
            self.max_ammo = 12
            self.base_damage = 50


    def fight(self):
        current_ammo = self.ammo
        self.ammo = 0
        return self.base_damage * current_ammo


    def refill(self, amount_of_ammo):
        if self.ammo == self.max_ammo:
            return amount_of_ammo
        elif self.ammo + amount_of_ammo < self.max_ammo:
            self.ammo = self.ammo + amount_of_ammo
            return 0
        else:
            return_ammo = amount_of_ammo - self.max_ammo
            self.ammo = self.max_ammo
            return return_ammo


    def get_type(self):
        return self.aircraft_type


    def get_status(self):
        return "Type: " + self.aircraft_type + " Ammo: " + str(self.ammo) + " Base damage: " + str(self.base_damage) + " All damage: " + str(self.ammo*self.base_damage)


class Carrier(object):
    def __init__(self, ammo, hp):
        self.ammo = ammo
        self.aircrafts = []
        self.hp = hp


    def add_aircraft(self, aircraft_type):
        self.aircrafts.append(Aircraft(aircraft_type))

    
    def fill(self):
        if self.ammo == 0:
            raise Exception('No ammo!')
        for aircraft in self.aircrafts:
            if aircraft.get_type == "f35":
                self.ammo = aircraft.refill(self.ammo)
        for aircraft in self.aircrafts:
            self.ammo = aircraft.refill(self.ammo)


    def fight(self, carrier):
        sum_of_damage = 0
        for aircraft in self.aircrafts:
            sum_of_damage += aircraft.fight()
        carrier.hp -= sum_of_damage


    def get_status(self):
        sum_of_damage = 0
        for aircraft in self.aircrafts:
            sum_of_damage += aircraft.ammo * aircraft.base_damage
        base_status = "HP: " + str(self.hp) + ", Aircraft count: " + str(len(self.aircrafts)) + ", Ammo Storage: " + str(self.ammo) + ", Total damage: " + str(sum_of_damage)
        base_status += "Aircrafts:\n"
        for aircraft in self.aircrafts:
            base_status += aircraft.get_status() + "\n"
        return base_status 


carrier = Carrier(5000, 3000)
carrier.add_aircraft("f16")
carrier.add_aircraft("f16")
carrier.add_aircraft("f16")
carrier.add_aircraft("f35")
print(carrier.get_status())
carrier.fill()
print(carrier.get_status())
            
