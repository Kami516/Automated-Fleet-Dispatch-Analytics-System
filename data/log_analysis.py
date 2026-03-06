import pandas as pd

def get_vehicle_route():
    df = pd.read_csv('data/vehicle_logs.csv')
    df = df.groupby('vehicle')['location'].unique().reset_index()
    df['location'] = df['location'].apply(lambda x: list(x) + ['Warsaw'])

    df = df.rename(columns={'location':'route'})

    return df

def get_net_profit_per_vehicle():
    df = pd.read_csv('data/vehicle_logs.csv')
    result = df[df['action'] == 'return'].copy()
    result['net_profit'] = result['cost_of_package'] - (result['cost_of_fuel'] + result['driver_salary'])

    return result