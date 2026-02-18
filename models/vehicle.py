class Vehicle:
    def __init__(self,name,max_load,fuel_max,fuel_consumption):
        self.name = name
        self.max_load = max_load
        self.fuel_max = fuel_max
        self.fuel_consumption= fuel_consumption

        self.current_load = []
        self.fuel_current = []



    def drive(self,distance):
        pass

    def refuel(self,amount):
        pass

    def load(self,package):
        pass

class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name,max_load=1000,fuel_max=500,fuel_consumption=25)

class Van(Vehicle):
    def __init__(self, name):
        super().__init__(name, max_load=300, fuel_max=150,fuel_consumption=15)
