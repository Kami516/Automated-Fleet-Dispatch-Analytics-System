from models.package import Package
from models.vehicle import Truck
from models.vehicle import Van
from utils import map_utils
import pandas as pd
from services.fleet_manager import dispatcher

def manager():
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

    print(df)
    return df

def fuel_consumption(df):
    routes = df.groupby('vehicle')['destination'].unique()
    print(routes)
    


def main():
    print("Hello from logistics-fleet-simulator!")
    df = manager()
    fuel_consumption(df)


if __name__ == "__main__":
    main()
