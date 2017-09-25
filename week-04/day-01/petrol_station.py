class Station(object):
    def __init__(self):
        self.gasAmount = 1500

    def refill(self):
        self.gasAmount -= Car.capacity
        Car.gas_amount += Car.capacity

class Car(object):
    gas_amount = 0
    capacity = 100
        

station_01 = Station()
car_01 = Car()

station_01.refill()
print(station_01.gasAmount)