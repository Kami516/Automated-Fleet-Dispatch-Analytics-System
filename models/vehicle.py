class Vehicle:
    def __init__(self,name,max_load,fuel_max,fuel_consumption):
        self.name = name
        self.max_load = max_load
        self.fuel_max = fuel_max
        self.fuel_consumption= fuel_consumption

        self.current_load = []
        self.fuel_current = fuel_max



    def drive(self,distance):
        pass

    def refuel(self,amount):
        pass

    def load(self,package):
        current_weight = sum(p.weight for p in self.current_load)

        if (current_weight + package.weight) <= self.max_load:
            self.current_load.append(package)
            print(f'Package {package.id}, with weight: {package.weight}, loaded succesfully, current {self.name} load : {sum(p.weight for p in self.current_load)}')
        else:
            print(f'Package {package.id}, with weight: {package.weight}, is to heavy for this vehicle, max load : {self.max_load}, current_load: {current_weight}')

class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name,max_load=1000,fuel_max=500,fuel_consumption=25)

class Van(Vehicle):
    def __init__(self, name):
        super().__init__(name, max_load=150, fuel_max=150,fuel_consumption=15)
