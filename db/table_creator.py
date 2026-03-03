import sqlite3
from models.vehicle import Truck
from models.vehicle import Van

def create_tables():
    script =(
        '''DROP TABLE IF EXISTS Packages;
        CREATE TABLE IF NOT EXISTS Packages(
        id INTEGER PRIMARY KEY,
        weight INTEGER,
        volume REAL,
        destination TEXT,
        region TEXT,
        status INTEGER
        );

        DROP TABLE IF EXISTS Vehicles;
        CREATE TABLE IF NOT EXISTS Vehicles(
        id INTEGER PRIMARY KEY,
        name TEXT,
        position TEXT,
        max_load INTEGER,
        volume_capacity REAL,
        fuel_max INTEGER,
        fuel_consumption INTEGER,
        region TEXT,
        type TEXT
        );
        '''
    )

    return script

def insert_packages():

    data = [
        # North
        (11, 350, 3.5, 'Gdansk', 'North', 0),
        (12, 120, 0.8, 'Gdansk', 'North', 0),
        (13, 15, 0.1, 'Szczecin', 'North', 0),
        (14, 200, 1.5, 'Szczecin', 'North', 0),
        (29, 85, 0.6, 'Bialystok', 'North', 0),
        (30, 10, 0.1, 'Bialystok', 'North', 0),
        
        # South
        (15, 400, 3.0, 'Katowice', 'South', 0),
        (16, 50, 0.4, 'Katowice', 'South', 0),
        (17, 75, 0.5, 'Krakow', 'South', 0),
        (18, 5, 0.05, 'Rzeszow', 'South', 0),
        (19, 180, 1.2, 'Rzeszow', 'South', 0),
        
        # West
        (25, 140, 1.0, 'Poznan', 'West', 0),
        (26, 60, 0.4, 'Poznan', 'West', 0),
        (27, 300, 2.0, 'Wroclaw', 'West', 0),
        (28, 45, 0.3, 'Wroclaw', 'West', 0),
        
        # Center
        (23, 250, 1.8, 'Lodz', 'Center', 0),
        (24, 20, 0.2, 'Lodz', 'Center', 0)
    ]

    script = (
        '''INSERT INTO Packages(id,weight,volume,destination,region,status) VALUES (?,?,?,?,?,?);
        '''
    )

    return script,data


def insert_vehicles():
    fleet_cars = {
        'North' : [Truck('Man_North'),Van('Sprinter_North')],
        'South' : [Truck('Scania_South'),Van('Berlingo_South')],
        'West' : [Truck('Volvo_West')],
        'Center' : [Truck('Daf_Center')]     
    }

    with sqlite3.connect('logistics_fleet.db') as conn:

        cur = conn.cursor()
        query = '''INSERT INTO Vehicles (name, position, max_load,volume_capacity, fuel_max, fuel_consumption, region, type)
        VALUES(?,?,?,?,?,?,?,?)          
        '''

        for region_name, vehicle_list in fleet_cars.items():
            for v in vehicle_list:

                values=(
                    v.name,
                    v.position,
                    v.max_load,
                    v.volume_capacity,
                    v.fuel_max,
                    v.fuel_consumption,
                    region_name,
                    v.__class__.__name__
                )
                cur.execute(query,values)
                conn.commit()

    return fleet_cars


def create_db():
    create_packages_script = create_tables()
    insert_packages_script,data = insert_packages()

    with sqlite3.connect('logistics_fleet.db') as conn:
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
        cur.executescript(create_packages_script)
        print('Data Base created succesfully')
        cur.executemany(insert_packages_script,data)
        conn.commit()
        print(f'Added {len(data)} packages into data base!')

    insert_vehicles()