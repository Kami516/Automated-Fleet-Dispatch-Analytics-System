class Vehicle:
    def __init__(self,name,position,max_load,fuel_max,fuel_consumption):
        self.name = name
        self.position = position
        self.max_load = max_load
        self.fuel_max = fuel_max
        self.fuel_consumption= fuel_consumption

        self.current_load = []
        self.fuel_current = fuel_max

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name} (Max: {self.max_load})"

    def drive(self,distance):
        fuel_needed = (distance / 100) * self.fuel_consumption
        if (self.fuel_current -fuel_needed) > 0:
            self.fuel_current = round(self.fuel_current -fuel_needed,2)
            print(f'{self.name}, {self.fuel_current}/{self.fuel_max}')
        else:
            print(f'{self.name} doesnt have enough fuel: {self.fuel_current}/{self.fuel_max}')
            self.refuel(self.fuel_max-self.fuel_current)
            self.fuel_current = round(self.fuel_current -fuel_needed,2)
            print(f'{self.name}, {self.fuel_current}/{self.fuel_max}')

    def refuel(self,amount):
        self.fuel_current = self.fuel_current + amount
        print(f'Vehicle :{self.name}, refuel succesfully {amount}l, fuel status: {self.fuel_current}/{self.fuel_max}')

    def load(self,package):
        current_weight = sum(p.weight for p in self.current_load)

        if (current_weight + package.weight) <= self.max_load:
            self.current_load.append(package)
            print(f'Package {package.id}, with weight: {package.weight}, loaded succesfully, current {self.name} load : {sum(p.weight for p in self.current_load)}')
            return True
        else:
            print(f'Package {package.id}, with weight: {package.weight}, is to heavy for this vehicle, max load : {self.max_load}, current_load: {current_weight}')
            return False

class Truck(Vehicle):
    def __init__(self, name, position='Warsaw'):
        super().__init__(name,position,max_load=600,fuel_max=500,fuel_consumption=35)

class Van(Vehicle):
    def __init__(self, name, position='Warsaw'):
        super().__init__(name,position, max_load=220, fuel_max=50,fuel_consumption=15)
