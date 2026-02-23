import sqlite3
import pandas as pd
from models.package import Package
from models.vehicle import Truck
from models.vehicle import Van

def load_data_from_db():
    conn = sqlite3.connect('logistics_fleet.db')

    df_packages = pd.read_sql_query("SELECT * FROM Packages", conn)
    conn.close()

    df_packages['status'] = df_packages['status'].astype(bool)
    packages = [Package(*row) for row in df_packages.itertuples(index=False)]

    return df_packages,packages

def load_fleet_from_db():
    fleet_cars = {}
    conn = sqlite3.connect('logistics_fleet.db')
    df_vehicles = pd.read_sql_query("SELECT * FROM Vehicles", conn)
    conn.close()

    for vehicle in df_vehicles.itertuples(index=False):
        if vehicle.type == 'Van':
            new_vehicle = Van(vehicle.name, vehicle.position)
        elif vehicle.type == 'Truck':
            new_vehicle = Truck(vehicle.name, vehicle.position)

        fleet_cars.setdefault(vehicle.region,[]).append(new_vehicle)

    return fleet_cars

def package_update_db(df):
    conn = sqlite3.connect('logistics_fleet.db')
    cursor = conn.cursor()

    loaded_packages = df[df['status']==True]

    for index,row in loaded_packages.iterrows():
        query = "UPDATE Packages SET status = 1 WHERE id = ?"

        cursor.execute(query, (row['id'],))

    conn.commit()
    conn.close()