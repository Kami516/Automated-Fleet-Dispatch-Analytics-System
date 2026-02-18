from models.package import Package
from models.vehicle import Truck
from models.vehicle import Van
from utils import map_utils
import pandas as pd
from services.fleet_manager import dispatcher

def manager():
    t1 = Truck('Man')
    t2 = Truck('Scania')
    t3 = Truck('Volvo')
    v1 = Van('Sprinter')
    v2 = Van('Berlingo')

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

    north = []
    south = []
    west = []
    center = []
    for package in data:
        if package['region'] == 'North':
            north.append(package)
        elif package['region'] == 'South':
            south.append(package)
        elif package['region'] == 'West':
            west.append(package)
        elif package['region'] == 'Center':
            center.append(package)

    north_df = pd.DataFrame(north)
    south_df = pd.DataFrame(south)
    west_df = pd.DataFrame(west)
    center_df = pd.DataFrame(center)
            

    # for package in df:
    #     # for region in package['region']:
    #     #     if region == grouped_regions['region'][1]:
    #     #         print(f'{package}  {region} {grouped_regions['region'][1]}')
    #     print( package)
            




def main():
    print("Hello from logistics-fleet-simulator!")
    manager()


if __name__ == "__main__":
    main()
