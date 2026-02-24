class Vehicle:
    def __init__(self,name,position,max_load,fuel_max,fuel_consumption):
        self.name = name
        self.position = position
        self.max_load = max_load
        self.fuel_max = fuel_max
        self.fuel_consumption= fuel_consumption

        self.current_load = []
        self.fuel_current = fuel_max

        self.log_entry = []
        self.fuel_used = 0
        self.fuel_avg_price = 5.65
        self.fuel_cost = 0.0

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name} (Max: {self.max_load})"
    
    def add_log(self,name,action,location,distance_km,fuel_left,details,fuel_cost):
        new_log = {
            'vehicle': name,
            'action': action,
            'location': location,
            'distance_km': distance_km,
            'fuel_left': round(fuel_left,2),
            'details': details,
            'price_of_fuel' : fuel_cost
        }
        self.log_entry.append(new_log)

    def drive(self,distance):

        fuel_needed = (distance / 100) * self.fuel_consumption
        self.fuel_used = self.fuel_used + fuel_needed

        if (self.fuel_current -fuel_needed) >= 0:

            self.fuel_current = round(self.fuel_current -fuel_needed,2)
            print(f'{self.name}, {self.fuel_current}/{self.fuel_max}')
            self.fuel_cost = float(self.fuel_used*self.fuel_avg_price)
            self.add_log(self.name,'drive',self.position,distance,self.fuel_max-self.fuel_current,f'Route completed with fuel usage: {self.fuel_used}',self.fuel_cost)

        else:
            while (self.fuel_current -fuel_needed) < 0:
                print(f'{self.name} doesnt have enough fuel: {self.fuel_current}/{self.fuel_max}')
                fuel_needed = fuel_needed -self.fuel_current
                self.fuel_current = 0
                self.refuel(self.fuel_max)
                print(f'{self.name}, refueled to {self.fuel_current}/{self.fuel_max}')
            self.fuel_current = round(self.fuel_current - fuel_needed, 2)
            print(f'{self.name} arrived at destination, {self.fuel_current}/{self.fuel_max}')
            self.fuel_cost = float(self.fuel_used*self.fuel_avg_price)
            self.add_log(self.name, 'drive', self.position, distance, self.fuel_current, f'Route completed with fuel usage: {self.fuel_used}',self.fuel_cost)

    def refuel(self,amount):
        self.fuel_current = self.fuel_max
        print(f'Vehicle :{self.name}, refuel succesfully, fuel status: {self.fuel_current}/{self.fuel_max}')
        self.fuel_cost = float(self.fuel_used*self.fuel_avg_price)
        self.add_log(self.name,'refuel',self.position,'0',self.fuel_max-self.fuel_current,f'refuel: {amount}',self.fuel_cost)

    def load(self,package):
        current_weight = sum(p.weight for p in self.current_load)

        if (current_weight + package.weight) <= self.max_load:
            self.current_load.append(package)
            self.fuel_cost = float(self.fuel_used*self.fuel_avg_price)
            print(f'Package {package.id}, with weight: {package.weight}, loaded succesfully, current {self.name} load : {sum(p.weight for p in self.current_load)}')
            self.add_log(self.name,'load',self.position,'0',self.fuel_max-self.fuel_current,f'loaded: {package.id}, with weight: {package.weight}',self.fuel_cost)
            return True
        else:
            print(f'Package {package.id}, with weight: {package.weight}, is to heavy for this vehicle, max load : {self.max_load}, current_load: {current_weight}')
            return False
        
        
    def return_to_base(self,position,distance):
        self.drive(distance)
        self.position = position
        self.add_log(self.name,'drive',self.position,distance,self.fuel_max-self.fuel_current,f'Succesfully returned to base in {position}, with fuel usage: {self.fuel_used}',self.fuel_cost)

class Truck(Vehicle):
    def __init__(self, name, position='Warsaw'):
        super().__init__(name,position,max_load=600,fuel_max=500,fuel_consumption=35)

class Van(Vehicle):
    def __init__(self, name, position='Warsaw'):
        super().__init__(name,position, max_load=220, fuel_max=50,fuel_consumption=15)
