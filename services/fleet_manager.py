from models.package import Package
from models.vehicle import Truck
from models.vehicle import Van
from utils import map_utils
import pandas as pd
from utils.map_utils import dist_calc

def load_data():
    fleet_cars = {
        'North' : [Truck('Man_North'),Van('Sprinter_North')],
        'South' : [Truck('Scania_South'),Van('Berlingo_South')],
        'West' : [Truck('Volvo_West')],
        'Center' : [Truck('Daf_Center')]     
    }

    packages = []

    # North
    packages.append(Package(11, 350, 'Gdansk', 'North', False))
    packages.append(Package(12, 120, 'Gdansk', 'North', False))
    packages.append(Package(13, 15, 'Szczecin', 'North', False))
    packages.append(Package(14, 200, 'Szczecin', 'North', False))
    packages.append(Package(29, 85, 'Bialystok', 'North', False))
    packages.append(Package(30, 10, 'Bialystok', 'North', False))

    # South
    packages.append(Package(15, 400, 'Katowice', 'South', False))
    packages.append(Package(16, 50, 'Katowice', 'South', False))
    packages.append(Package(17, 75, 'Cracow', 'South', False))
    packages.append(Package(18, 5, 'Rzeszow', 'South', False))
    packages.append(Package(19, 180, 'Rzeszow', 'South', False))

    # West
    packages.append(Package(25, 140, 'Poznan', 'West', False))
    packages.append(Package(26, 60, 'Poznan', 'West', False))
    packages.append(Package(27, 300, 'Wroclaw', 'West', False))
    packages.append(Package(28, 45, 'Wroclaw', 'West', False))

    # Center
    packages.append(Package(23, 250, 'Lodz', 'Center', False))
    packages.append(Package(24, 20, 'Lodz', 'Center', False))

    data = [p.__dict__ for p in packages]
    df = pd.DataFrame(data)

    return (df, fleet_cars,packages)

def load_packages(df, fleet_cars,packages):

    print(f"----{len(packages)} Packages to sent today----")
    print (df)

    print('\nGrouped by regions:')
    grouped_regions = dispatcher(df)
    print(grouped_regions)

    grouped = df.groupby('region')

    for region_name, region_df in grouped:

        print(f'-->{region_name}')
        sorted_df = region_df.sort_values('weight', ascending=False)
        vehicles_in_region = fleet_cars.get(region_name,[])
        if not vehicles_in_region:
            print(f'Region {region_name}, doesnt have any free cars')
            continue

        print(vehicles_in_region)

        for index,row in sorted_df.iterrows():

            package = Package(
                id=row['id'],
                weight=row['weight'],
                status=row['status'],
                destination=row['destination'],
                region=row['region']
            )
            is_loaded=False

            for vehicle in vehicles_in_region:
                if(vehicle.load(package)):
                    is_loaded=True
                    df.loc[index, 'status']=True
                    df.loc[index, 'vehicle']=vehicle.name
                    break
            if not is_loaded:
                print(f"Cannot load package {row['id']}, {row['weight']}")
    
    return df

def simulate_routes(df,fleet_cars):
    routes = df.groupby('vehicle')['destination'].unique().reset_index()
    base_location = 'Warsaw'
    
    for index,row in routes.iterrows():
        print(row['vehicle'])
        drives = 0
        cities_left = list(row['destination'])
        for region, vehicle_list in fleet_cars.items():
            for vehicle in vehicle_list:
                if(vehicle.name == row['vehicle']):
                    current_vehicle = vehicle
                    break

        while drives < len(row['destination']):
            distance_min = 5000
            closest = ''

            for x  in cities_left:
                distance = dist_calc(current_vehicle.position,x)
                print(distance,x)
                if distance < distance_min:
                    distance_min = distance
                    closest = x
            print(f'Min distance for {row['vehicle']}: {round(distance_min,2)} {current_vehicle.position} ->{closest}')
            current_vehicle.drive(distance_min)
            current_vehicle.position = closest
            cities_left.remove(closest)
            drives = drives + 1

        distance = dist_calc(current_vehicle.position,base_location)
        print(f'Returning to base in {base_location}, {distance}')
        current_vehicle.drive(distance)
        current_vehicle.position = base_location


def dispatcher(df):
    grouped = df.groupby('region')['weight'].sum().reset_index().sort_values(by='weight', ascending=False)

    return grouped