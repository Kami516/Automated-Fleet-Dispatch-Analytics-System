import pandas as pd
from models.vehicle import Truck,Van

def vehicle_log_add(fleet_cars):
    vehicle_logs = []
    for region, vehicle_list in fleet_cars.items():
        for vehicle in vehicle_list:
            vehicle_logs.extend(vehicle.log_entry)

    df = pd.DataFrame.from_dict(vehicle_logs)
    df.to_csv('data/vehicle_logs.csv', index=False)

def package_log_add(df):
    df = df.rename(columns={'status':'is_delivered'})
    df.to_csv('data/package_logs.csv',index=False)