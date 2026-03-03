from models.package import Package
from models.vehicle import Truck
from models.vehicle import Van
from utils import map_utils
import pandas as pd
from utils.map_utils import dist_calc
from data.log_creator import vehicle_log_add,package_log_add
from db.loader import load_data_from_db,package_update_db,load_fleet_from_db

def load_data():

    df,packages = load_data_from_db()
    fleet_cars = load_fleet_from_db()

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
                volume=row['volume'],
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
    
    package_log_add(df)
    package_update_db(df)
    
    return df

def simulate_routes(df,fleet_cars):
    routes = df.groupby('vehicle')['destination'].unique().reset_index()
    base_location = 'Warsaw'
    
    for index,row in routes.iterrows():
        print(row['vehicle'])
        drives = 1
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
            current_vehicle.position = closest
            current_vehicle.drive(distance_min)
            cities_left.remove(closest)
            drives = drives + 1

        distance = dist_calc(current_vehicle.position,base_location)
        print(f'Returned to base in {base_location}, {distance}')
        current_vehicle.return_to_base(base_location,distance)

    vehicle_log_add(fleet_cars)



def dispatcher(df):
    grouped = df.groupby('region')['weight'].sum().reset_index().sort_values(by='weight', ascending=False)

    return grouped 