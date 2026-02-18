from models.package import Package
from models.vehicle import Truck
from models.vehicle import Van
from utils import map_utils

def manager():
    t1 = Truck('Man')
    t2 = Truck('Scania')
    v1 = Van('Sprinter')

    packages = []

    packages.append(Package(1, 25, 'Cracow', False))
    packages.append(Package(2, 3, 'Wroclaw', False))
    packages.append(Package(3, 150, 'Gdansk', False))
    packages.append(Package(4, 10, 'Poznan', False))
    packages.append(Package(5, 2, 'Warsaw', False))
    packages.append(Package(6, 45, 'Rzeszow', False))
    packages.append(Package(7, 5, 'Szczecin', False))
    packages.append(Package(8, 80, 'Katowice', False))
    packages.append(Package(9, 12, 'Bialystok', False))
    packages.append(Package(10, 30, 'Lodz', False))

    print(f"----{len(packages)} Packages to sent today----")
    for package in packages:
        print(f'{package.id} | wieght: {package.weight} | destination: {package.destination}')

    v1.load(packages[0])
    v1.load(packages[1])
    v1.load(packages[4])
    v1.load(packages[2])


def main():
    print("Hello from logistics-fleet-simulator!")
    manager()


if __name__ == "__main__":
    main()
