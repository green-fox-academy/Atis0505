from Aircraft import Aircraft

class Carrier():
    def __init__(self, store_of_ammo, healt_point):
        self.list_of_aircraft = []
        self.store_of_ammo = store_of_ammo
        self.healt_point = healt_point


    def addAircraft(self, aircraft):
        self.list_of_aircraft.append(aircraft)


    def fill(self):
        for item in self.list_of_aircraft:
            if item.getType() == "F35":
                self.store_of_ammo = item.refill(self.store_of_ammo)
        for item in self.list_of_aircraft:
            if item.getType() == "F16":
                self.store_of_ammo = item.refill(self.store_of_ammo)
        
    def fight(self, Carrier):
        carrier_max_dmg = 0
        for item in self.list_of_aircraft:
            carrier_max_dmg += item.fight()
        Carrier.healt_point -= carrier_max_dmg 
        if Carrier.healt_point >= 0:
            self.getStatus()
        else:
            print("Dead!")    

    def getStatus(self):
        carrier_max_dmg = 0
        for item in self.list_of_aircraft:
            carrier_max_dmg += item.fight()
        print("HP: {}, Aircrfat count: {}, Ammo Storage: {}, Total damage: {}".format(self.healt_point, len(self.list_of_aircraft), self.store_of_ammo, carrier_max_dmg ))
        for item in self.list_of_aircraft:
            item.getStatus()
        

carrier = Carrier(3000,5000)

aircraft01 = Aircraft("F35")
carrier.addAircraft(aircraft01)
aircraft02 = Aircraft("F16")
carrier.addAircraft(aircraft02)
aircraft03 = Aircraft("F35")
carrier.addAircraft(aircraft03)
aircraft04 = Aircraft("F16")
carrier.addAircraft(aircraft04)
aircraft05 = Aircraft("F35")
carrier.addAircraft(aircraft05)
aircraft06 = Aircraft("F16")
carrier.addAircraft(aircraft06)
aircraft07 = Aircraft("F35")
carrier.addAircraft(aircraft07)
aircraft08 = Aircraft("F35")
carrier.addAircraft(aircraft08)
aircraft09 = Aircraft("F16")
carrier.addAircraft(aircraft09)
aircraft10 = Aircraft("F35")
carrier.addAircraft(aircraft10)
aircraft11 = Aircraft("F16")
carrier.addAircraft(aircraft11)
aircraft12 = Aircraft("F35")
carrier.addAircraft(aircraft12)

carrier.getStatus()
carrier.fill()
carrier.getStatus()