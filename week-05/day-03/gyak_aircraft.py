class Aircraft(object):
    def __init__(self, aircraft_type):
        self.aircraft_type = aircraft_type
        self.ammo = 0
        if aircraft_type == "F16":
            self.max_ammo = 8
            self.base_damage = 30
        elif aircraft_type == "F35":
            self.max_ammo = 12
            self.base_damage = 50

    
    def fight(self):
        current_ammo = self.ammo
        self.ammo = 0
        return self.base_damage * current_ammo


    def refill(self, carrier_ammo):
        if self.ammo == self.max_ammo:
            return carrier_ammo
        elif self.ammo + carrier_ammo < self.max_ammo:
            self.ammo = self.ammo + carrier_ammo
            return 0
        else:
            return_ammo = carrier_ammo - self.max_ammo
            self.ammo = self.max_ammo
            return return_ammo



    def get_type(self):
        return self.aircraft_type


    def get_status(self):
        return "Type "+self.get_type()+", Ammo: "+str(self.ammo)+", Base Damage: "+str(self.base_damage)+", All Damage: "+str(self.ammo*self.base_damage)


class Carrier(object):
    def __init__(self, ammo_store, health_point):
        self.ammo_store = ammo_store
        self.health_point = health_point
        self.list_of_aircrafts = []

    
    def addAircraft(self, aircraft_type):
        self.list_of_aircrafts.append(Aircraft(aircraft_type))


    def fill(self):
        if self.ammo_store == 0:
            raise Exception('No ammo!')
        for aircraft in self.list_of_aircrafts:
            if aircraft.get_type == "F35":
                self.ammo_store = aircraft.refill(self.ammo_store)
        for aircraft in self.list_of_aircrafts:
            self.ammo_store = aircraft.refill(self.ammo_store)
        


    def fight(self, other_carrier):
        full_damage = 0
        for aircraft in self.list_of_aircrafts:
            full_damage += aircraft.fight()
        other_carrier.health_point -= full_damage

    
    def getStatus(self):
        if self.health_point <=0:
            print("It's dead Jim :(")
        else:
            full_damage = 0
            for aircraft in self.list_of_aircrafts:
                full_damage += (aircraft.ammo * aircraft.base_damage)
            Status = "HP: "+str(self.health_point)+", Aircraft count: "+ str(len(self.list_of_aircrafts)) +", Ammo Storage: "+str(self.ammo_store)+", Total Damage: "+str(full_damage)+"\n"
            Status += "Aircrafts:\n"
            for aircraft in self.list_of_aircrafts:
                Status += aircraft.get_status() + "\n"
            return Status
            

carrier = Carrier(5000, 3000)
carrier02 = Carrier(6000, 1500)
carrier.addAircraft("F16")
carrier.addAircraft("F16")
carrier.addAircraft("F16")
carrier.addAircraft("F35")
carrier.addAircraft("F16")
carrier02.addAircraft("F35")
carrier02.addAircraft("F16")
carrier02.addAircraft("F35")
carrier02.addAircraft("F16")
carrier02.addAircraft("F35")
print(carrier.getStatus())
carrier.fill()
carrier.fight(carrier02)
print(carrier.getStatus())
print(carrier02.getStatus())